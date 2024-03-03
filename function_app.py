import json

from azure.functions import FunctionApp, AuthLevel, HttpRequest, HttpResponse

from src.handlers.add_barcodes import add_barcodes_handler
from src.handlers.home import home_handler
from src.handlers.link_shop import link_shop_handler
from src.handlers.parse_from_url import parse_from_url_handler
from src.helpers.logging import set_logger

logger = set_logger()

app = FunctionApp(http_auth_level=AuthLevel.ANONYMOUS)


@app.route(route="home", methods=["GET"])
def home(req: HttpRequest) -> HttpResponse:  # pylint: disable=unused-argument
    return build_response(*home_handler(), mimetype="text/html")


@app.route(route="parse-from-url", methods=["POST"])
def parse_from_url(req: HttpRequest) -> HttpResponse:
    url, user_id = get_form_data(req, "url", "user_id")
    logger.info("URL: %s", url)
    logger.info("User ID: %s", user_id)
    return build_response(*parse_from_url_handler(url, user_id, logger))


@app.route(route="link-shop", methods=["POST"])
def link_shop(req: HttpRequest) -> HttpResponse:
    url, user_id, receipt_id = get_form_data(req, "url", "user_id", "receipt_id")
    return build_response(*link_shop_handler(url, user_id, receipt_id, logger))


@app.route(route="add-barcodes", methods=["POST"])
def add_barcodes(req: HttpRequest) -> HttpResponse:
    shop_id, items = get_form_data(req, "shop_id", "items")
    return build_response(*add_barcodes_handler(shop_id, json.loads(items), logger))


def get_form_data(req: HttpRequest, *args: str) -> tuple[str, ...]:
    return tuple(req.form.get(val).strip() for val in args)


def build_response(
    status: int, body: str | dict, mimetype: str = "application/json"
) -> HttpResponse:
    if status >= 400:
        logger.error("%s %s", status, body["msg"])
    return HttpResponse(
        body=body if isinstance(body, str) else json.dumps(body),
        status_code=status,
        mimetype=mimetype,
        headers={"access-control-allow-origin": "*"},
    )
