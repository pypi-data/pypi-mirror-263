import time

from eip712_structs import EIP712Struct
from eth_account import Account
from web3 import Web3

from bsx_python_sdk.client.rest.base import RestClient
from bsx_python_sdk.client.rest.account.types import SignKey, Register
from bsx_python_sdk.common.types.account import RegisterParams, BSXApiKey


class AccountClient(RestClient):
    domain_signature: EIP712Struct

    def __init__(self, domain: str, domain_signature: EIP712Struct):
        super().__init__(domain)
        self.domain_signature = domain_signature

    def register(self, params: RegisterParams) -> BSXApiKey:
        wallet = Account.from_key(params.wallet_pkey)
        signer = Account.from_key(params.signer_pkey)

        signable_wallet = SignKey(account=wallet.address)
        signable_signer_bytes = Web3.keccak(signable_wallet.signable_bytes(domain=self.domain_signature))
        signer_signature = Account._sign_hash(signable_signer_bytes, signer.key).signature.hex()

        nonce = round(time.time())
        signable_message = Register(key=signer.address, message=params.message, nonce=nonce)
        signable_message_bytes = Web3.keccak(signable_message.signable_bytes(domain=self.domain_signature))
        account_signature = Account._sign_hash(signable_message_bytes, wallet.key).signature.hex()

        payload = {
            "user_wallet": wallet.address,
            "signer": signer.address,
            "nonce": nonce,
            "wallet_signature": account_signature,
            "signer_signature": signer_signature,
            "message": params.message,
        }

        resp = self.post("/users/register", payload)
        return BSXApiKey(**resp)
