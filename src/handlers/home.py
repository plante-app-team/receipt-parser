from http import HTTPStatus

from jinja2 import Environment, FileSystemLoader

from src.helpers.common import get_templates_dir
from src.schemas.common import ItemBarcodeStatus


def home_handler() -> (HTTPStatus, str):
    file_loader = FileSystemLoader(get_templates_dir())
    jinja = Environment(loader=file_loader)
    data = {
        "route": {
            "parse": "parse-from-url",
            "link_shop": "link-shop",
            "add_barcodes": "add-barcodes",
        },
        "barcode_status": {
            status.name.lower(): status.value for status in ItemBarcodeStatus
        },
    }
    return HTTPStatus.OK, jinja.get_template("home.html").render(data)
