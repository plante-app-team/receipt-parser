import os

from azure.functions import FunctionApp, AuthLevel, HttpRequest, HttpResponse
from jinja2 import Environment, FileSystemLoader

from src.adapters.db.cosmos_db_core import CosmosDBCoreAdapter
from src.helpers import get_html, build_response
from src.parsers.receipt_provider import ReceiptProvider
from src.schemas.common import EnvType, TableName

app = FunctionApp(http_auth_level=AuthLevel.ANONYMOUS)

file_loader = FileSystemLoader(os.path.join("src", "static", "templates"))
jinja = Environment(loader=file_loader)


@app.route(route="home", methods=["GET"])
def home(req: HttpRequest) -> HttpResponse:
    return HttpResponse(jinja.get_template("home.html").render(), mimetype="text/html")


@app.route(route="parse-from-url", methods=["POST"])
def parse_from_url(req: HttpRequest) -> HttpResponse:
    url = req.form.get("url")
    user_id = req.form.get("user_id")
    if not url:
        return build_response(400,"URL is required")

    try:
        receipt_provider = ReceiptProvider.from_url(url)
    except ValueError:
        return build_response(400,"Unsupported URL")

    receipt_html = get_html(url)
    parser = receipt_provider.get_parser()
    receipt = parser(user_id).parse_html(receipt_html).extract_data()

    session = CosmosDBCoreAdapter(EnvType.DEV).use_db(TableName.RECEIPT)
    session.create_one(receipt.to_dict())

    return build_response(200,"Receipt successfully processed")
