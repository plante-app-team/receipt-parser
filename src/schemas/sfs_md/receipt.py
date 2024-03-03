from dataclasses import dataclass
from datetime import datetime
from typing import List
from uuid import UUID

from src.schemas.common import CountryCode, CurrencyCode
from src.schemas.purchased_item import PurchasedItem
from src.schemas.receipt import Receipt


@dataclass
class SfsMdReceipt(Receipt):
    id: str | None
    date: datetime
    user_id: UUID
    company_id: str
    company_name: str
    country_code: CountryCode
    shop_address: str
    cash_register_id: str
    key: int
    currency_code: CurrencyCode
    total_amount: float
    purchases: List[PurchasedItem]
    receipt_url: str | None = None
    shop_id: UUID | None = None

    def __post_init__(self):
        if not isinstance(self.user_id, UUID):
            raise ValueError("User ID must be a UUID")

        if self.shop_id and not isinstance(self.shop_id, UUID):
            raise ValueError("Shop ID must be a UUID")

        self.id = f"{CountryCode.MOLDOVA}_{self.cash_register_id}_{self.key}".lower()
        self.country_code = CountryCode.MOLDOVA
        self.currency_code = CurrencyCode.MOLDOVAN_LEU
        self.receipt_url = (
            f"https://mev.sfs.md/receipt-verifier/{self.cash_register_id}/"
            f"{self.total_amount:.2f}/{self.key}/{self.date:%Y-%m-%d}"
        )
