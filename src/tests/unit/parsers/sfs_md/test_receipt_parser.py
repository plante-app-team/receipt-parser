import os
from unittest import TestCase
from unittest.mock import Mock
from uuid import UUID

from src.parsers.sfs_md.receipt_parser import SfsMdReceiptParser
from src.tests import load_stub_file, USER_ID_1
from src.tests.stubs.receipts.sfs_md.expected_objects import LIN_RECEIPT, KL_RECEIPT

LIN_RECEIPT_PATH = os.path.join("receipts", "sfs_md", "linella.html")
KL_RECEIPT_PATH = os.path.join("receipts", "sfs_md", "kaufland.html")
# pylint: disable=line-too-long
LIN_RECEIPT_URL = (
    "https://mev.sfs.md/receipt-verifier/J403001576/118.04/135932/2024-01-17"
)


class TestSfsMdReceiptParser(TestCase):
    @classmethod
    def setUpClass(cls):
        logger = Mock()
        cls.parser = SfsMdReceiptParser(logger)

    def test_parse(self):
        self.assertEqual(
            self.parser.parse_html(load_stub_file(KL_RECEIPT_PATH))
            .build_receipt(UUID(USER_ID_1))
            .receipt,
            KL_RECEIPT,
        )
        self.assertEqual(
            self.parser.parse_html(load_stub_file(LIN_RECEIPT_PATH))
            .build_receipt(UUID(USER_ID_1))
            .receipt,
            LIN_RECEIPT,
        )
