from dataclasses import dataclass, asdict
from datetime import datetime
from typing import List

from src.schemas.purchase import Purchase


@dataclass
class Receipt:
    user_id: int
    company_id: str
    company_name: str
    country_code: str
    shop_address: str
    cash_register_id: str
    receipt_id: int
    currency_code: str
    date: datetime
    total_amount: float
    purchases: List[Purchase]

    @property
    def id(self) -> str:
        return f"{self.cash_register_id}_{self.receipt_id}".lower()

    @property
    def receipt_url(self) -> str:
        return (
            f"https://mev.sfs.md/receipt-verifier/{self.cash_register_id}/"
            f"{self.total_amount:.2f}/{self.receipt_id}/{self.date:%Y-%m-%d}"
        )

    def to_dict(self):
        receipt = asdict(self)
        receipt["id"] = self.id
        receipt["date"] = self.date.isoformat()
        receipt["receipt_url"] = self.receipt_url
        return receipt
