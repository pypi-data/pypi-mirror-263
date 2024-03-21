# coding:utf-8

import os
from typing import Optional

import requests


def download(url: str, path: Optional[str] = None) -> Optional[str]:
    try:
        response = requests.get(url, headers={"User-Agent": "whatever"})
        if response.status_code != 200:
            return None

        disposition = response.headers.get("Content-Disposition")
        if not isinstance(disposition, str):
            return None

        def parse_filename(disposition: str) -> str:
            _, filename = disposition.split('=')
            return filename.strip('"').strip('"')

        filename = parse_filename(disposition)
        filepath = os.path.join(path if path else ".", filename)
        with open(filepath, "wb") as whdl:
            whdl.write(response.content)
        return filepath

    except Exception:
        return None
