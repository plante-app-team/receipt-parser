import os

from itertools import groupby

import requests


def get_templates_dir() -> str:
    return os.path.join("src", "static", "templates")


def get_template_path(template_name: str) -> str:
    return os.path.join(get_templates_dir(), template_name)


def split_list(lst, delimiter) -> list[list]:
    return [
        list(group) for key, group in groupby(lst, lambda x: x == delimiter) if not key
    ]


def get_html(url: str, logger) -> str | None:
    try:
        resp = requests.get(url, timeout=5)
        if resp.status_code == 200:
            return resp.text
        logger.warning("GET %s %s", url, resp.status_code)
    except requests.exceptions.ConnectionError as e:
        logger.error("GET %s %s", url, e)
    return None


def validate_barcode(barcode: str) -> bool:
    if len(barcode) not in (8, 12, 13, 14):
        return False

    total = 0
    for i, num in enumerate(barcode[:-1]):
        multiplier = (i + 1) % 2 if len(barcode) == 14 else i % 2
        total += int(num) * (1 + (2 * multiplier))

    return str((10 - (total % 10)) % 10) == barcode[-1]
