from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class BSXApiKey:
    api_key: str
    api_secret: str
    expired_at: datetime
    name: Optional[str]


@dataclass
class RegisterParams:
    wallet_pkey: str
    signer_pkey: str
    message: str
