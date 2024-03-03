from uuid import UUID

from src.helpers.common import get_html
from src.parsers.sfs_md.receipt_parser import SfsMdReceiptParser


def parse_from_url_handler(url: str, user_id: str, logger) -> (int, dict):
    if not url:
        return 400, {"msg": "URL is required"}

    try:
        user_id = UUID(user_id)
    except ValueError:
        return 400, {"msg": "Invalid user ID"}

    parser = SfsMdReceiptParser(logger)
    if not parser.validate_receipt_url(url):
        return 400, {"msg": "Unsupported URL"}

    receipt_html = get_html(url, logger)
    if not receipt_html:
        return 400, {"msg": "Failed to fetch receipt"}

    receipt = parser.parse_html(receipt_html).build_receipt(user_id).persist()

    return 200, {"msg": "Receipt successfully processed", "data": receipt.to_dict()}
