from abc import ABC, abstractmethod

from src.schemas.receipt import Receipt


class ReceiptParserBase(ABC):
    def __init__(self, user_id: int):
        self.user_id = user_id
        self._data: dict | None = None

    @abstractmethod
    def parse_html(self, page: str):
        pass

    @abstractmethod
    def extract_data(self) -> Receipt:
        pass
