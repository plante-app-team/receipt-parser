import os
from unittest import TestCase

from src.parsers.sfs_md.receipt_parser import SfsMdReceiptParser
from src.tests import load_stub_file
from src.tests.stubs.receipts.sfs_md.expected_objects import (
    KAUFLAND_RECEIPT,
    LINELLA_RECEIPT,
)


class TestSfsMdReceiptParser(TestCase):
    def test_parse(self):
        test_receipt_names = [
            os.path.join("receipts", "sfs_md", "linella.html"),
            os.path.join("receipts", "sfs_md", "kaufland.html"),
        ]
        receipts = []
        for file_name in test_receipt_names:
            receipts.append(
                SfsMdReceiptParser().parse_html(load_stub_file(file_name)).extract_data()
            )

        self.assertEqual(receipts, [KAUFLAND_RECEIPT, LINELLA_RECEIPT])
        self.assertEqual(
            receipts[0].receipt_url,
            "https://mev.sfs.md/receipt-verifier/J403001576/118.04/135932/2024-01-17",
        )
