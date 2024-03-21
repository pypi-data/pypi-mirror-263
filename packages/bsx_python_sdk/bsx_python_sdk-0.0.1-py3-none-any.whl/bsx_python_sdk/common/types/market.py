from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from enum import Enum
from typing import Optional, List


class Side(Enum):
    BUY = "BUY"
    SELL = "SELL"


@dataclass
class CreateOrderParams:
    side: Side
    product_index: int
    price: Decimal
    size: Decimal
    post_only = False
    reduce_only = False
    time_inf_force: str
    nonce: int


@dataclass
class Trade:
    id: str
    price: Decimal
    size: Decimal
    liquidity_indicator: int
    time: str
    funding_payment: str
    trading_fee: Decimal
    sequencer_fee: Decimal


@dataclass
class Order:
    id: str
    price: Decimal
    size: Decimal
    product_id: str
    side: str
    type: str
    time_in_force: str
    nonce: int
    post_only: bool
    reduce_only: bool
    created_at: datetime
    cancel_reason: str
    reject_reason: str
    cancel_reject_reason: str
    filled_fees: Decimal
    filled_size: Decimal
    status: str
    sender: str
    avg_price: Decimal
    cancel_requested: bool
    is_liquidation: bool
    initial_margin: str
    last_trades: list[Trade]


@dataclass
class CancelMultipleOrdersParams:
    product_ids: Optional[list[str]] = None
    order_ids: Optional[list[str]] = None
    nonces: Optional[list[int]] = None


@dataclass
class CancelOrderResult:
    order_id: str
    nonce: int


@dataclass
class CancelMultipleOrdersResult:
    cancelled_orders: list[CancelOrderResult]


@dataclass
class OrderListingResult:
    orders: list[Order]
