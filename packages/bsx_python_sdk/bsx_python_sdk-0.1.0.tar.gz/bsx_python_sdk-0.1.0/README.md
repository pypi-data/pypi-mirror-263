# BSX Exchange Python SDK

This is the Python SDK for the [BSX Exchange API](https://api-docs.bsx.exchange/reference/general-information).

See [SDK docs](https://bsx-exchange.github.io/vertex-python-sdk/index.html) to get started.

## Requirements

- Python 3.9 or above

## Installation

You can install the SDK via pip:

```bash
pip install bsx-exchange
```

## Basic usage

### Import the necessary

### Create a wallet and a signer from private keys

```python
from eth_account import Account

account = Account.from_key(
    "0x22f2f8bd71ba7dc47e762cc70b7e5db5ecc45ea4a7babc5268782c58c79c346e"
)
signer = Account.from_key(
    "0xdd86166bd13bbfa046967a9b8aa6e2e3c10a8b0bcef902fe63b01ba873148086"
)
```

### Create the BSXInstance providing BSX Exchange domain, account and signer:

```python
from bsx_python_sdk import BSXInstance

bsx_instance = BSXInstance(domain="https://api.testnet.bsx.exchange", wallet=account, signer=signer)
```

### Perform basic operations:

```python
# Placing orders
from bsx_python_sdk.common.types.market import CreateOrderParams

params = CreateOrderParams(
    side=Side.BUY,
    product_index=3,
    price=price,
    size=size,
    time_inf_force="GTC",
    nonce=int(time.time())
)
order = bsx_instance.create_order(params)
print("order id:", order.id)
```

See [Getting Started](https://bsx-exchange.github.io/vertex-python-sdk/getting-started.html) for more.

## Running locally

1. Clone [github repo](https://github.com/vertex-protocol/vertex-python-sdk)

2. Install poetry

```

$ curl -sSL https://install.python-poetry.org | python3 -

```

3. Setup a virtual environment and activate it

```

$ python3 -m venv venv
$ source ./venv/bin/activate

```

4. Install dependencies via `poetry install`