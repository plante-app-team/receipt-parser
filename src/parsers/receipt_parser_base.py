from abc import ABC, abstractmethod
from typing import Self
from uuid import UUID

from src.schemas.common import CountryCode, CurrencyCode
from src.schemas.receipt import Receipt


class ReceiptParserBase(ABC):
    receipt: Receipt
    hosts: list[str]
    country_code: CountryCode
    currency_code: CurrencyCode

    @abstractmethod
    def parse_html(self, page: str) -> Self:
        pass

    @abstractmethod
    def build_receipt(self, user_id: UUID) -> Self:
        pass

    @abstractmethod
    def persist(self) -> Self:
        pass
