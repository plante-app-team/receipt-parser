from enum import Enum

from src.parsers.receipt_parser_base import ReceiptParserBase
from src.parsers.sfs_md.receipt_parser import SfsMdReceiptParser


class ReceiptProvider(Enum):
    SFS_MD = {
        "hosts": ["https://mev.sfs.md", "https://sift-mev.sfs.md"],
        "parser": SfsMdReceiptParser,
    }

    @staticmethod
    def from_url(url: str):
        for provider in ReceiptProvider:
            if any(url.startswith(host) for host in provider.value.get("hosts")):
                return provider
        raise ValueError("Unsupported URL")

    def get_parser(self) -> ReceiptParserBase:
        return self.value.get("parser")
