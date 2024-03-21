import functools
from typing import Optional

import requests
from eip712_structs import make_domain
from eth_account.signers.local import LocalAccount

from bsx_python_sdk.client.rest.account.client import AccountClient
from bsx_python_sdk.client.rest.market.client import MarketClient
from bsx_python_sdk.common.exception import UnauthenticatedException
from bsx_python_sdk.common.types.account import RegisterParams
from bsx_python_sdk.common.types.market import CreateOrderParams, CancelOrderResult, CancelMultipleOrdersParams, \
    CancelMultipleOrdersResult, OrderListingResult, Order
from bsx_python_sdk.common.utils import AccountStorage


def refresh_api_key_if_needed(method):
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        try:
            return method(self, *args, **kwargs)
        except UnauthenticatedException:
            self.refresh_api_key_if_needed()
            return method(self, *args, **kwargs)
    return wrapper


class BSXInstance:
    def __init__(self, domain: str, wallet: LocalAccount, signer: LocalAccount):
        eip712_domain = self._build_eip712_domain(domain)
        self._account_client = AccountClient(domain=domain, domain_signature=eip712_domain)
        self._market_client = MarketClient(domain=domain, domain_signature=eip712_domain)

        api_key = self._account_client.register(
            RegisterParams(wallet_pkey=wallet.key, signer_pkey=signer.key, message="")
        )

        acc_storage = AccountStorage()
        acc_storage.set_signer(signer)
        acc_storage.set_wallet(wallet)
        acc_storage.set_api_key(api_key)

    @refresh_api_key_if_needed
    def create_order(self, params: CreateOrderParams) -> Order:
        return self._market_client.create_order(params)

    @refresh_api_key_if_needed
    def cancel_order(self, order_id: Optional[str], nonce: Optional[str]) -> CancelOrderResult:
        return self._market_client.cancel_order(order_id, nonce)

    @refresh_api_key_if_needed
    def cancel_orders(self, params: CancelMultipleOrdersParams) -> CancelMultipleOrdersResult:
        return self._market_client.cancel_orders(params)

    @refresh_api_key_if_needed
    def cancel_all_orders(self, product_id: str) -> CancelMultipleOrdersResult:
        return self._market_client.cancel_all_orders(product_id)

    @refresh_api_key_if_needed
    def get_open_orders(self, product_id: str) -> OrderListingResult:
        return self._market_client.get_open_orders(product_id)

    def _build_eip712_domain(self, domain: str):
        response = requests.get(domain + "/chain/configs")
        if response.status_code != 200:
            raise Exception(
                f"Failed to get chain config. Response code: {response.status_code}. "
                f"Response: {response.text}"
            )

        config = response.json()
        return make_domain(
            name=config["name"],
            version=config["version"],
            chainId=config["chain_id"],
            verifyingContract=config["verifying_contract"],  # note the changed naming convention here
        )

    def _refresh_api_key(self):
        acc_storage = AccountStorage()
        acquired_write_lock = acc_storage.lock_all_read()

        if acquired_write_lock:
            try:
                api_key = self._account_client.register(
                    RegisterParams(wallet_pkey=acc_storage.get_wallet_key(), signer_pkey=acc_storage.get_signer_key(), message="")
                )
                acc_storage.set_api_key(api_key)
            finally:
                acc_storage.release_all_read()

