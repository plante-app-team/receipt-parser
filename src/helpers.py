import json
from itertools import groupby

import requests
from azure.functions import HttpResponse


def split_list(lst, delimiter) -> list[list]:
    return [
        list(group) for key, group in groupby(lst, lambda x: x == delimiter) if not key
    ]


def get_html(url: str) -> str:
    return requests.get(url, timeout=5).text


def build_response(
    status: int, msg: str | None = None, data: list | dict | None = None
) -> HttpResponse:
    return HttpResponse(
        body=json.dumps({"message": msg, "data": data}),
        status_code=status,
        headers={"access-control-allow-origin": "*"},
    )
