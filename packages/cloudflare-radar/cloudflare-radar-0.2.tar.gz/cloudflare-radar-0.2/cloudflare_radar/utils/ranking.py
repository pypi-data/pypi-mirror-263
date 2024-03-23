# coding:utf-8

import csv
import os
from typing import Optional

from pycountry.db import Country
from xarg import commands

from .request import download


class domain_ranking(list):
    PREFIX = "http://radar.cloudflare.com/charts/TopDomainsTable"

    def __init__(self, location: Optional[Country] = None):
        self.__location: Optional[Country] = location
        super().__init__()

    @property
    def location(self) -> str:
        return self.__location.name if self.__location else "Worldwide"

    @property
    def url(self) -> str:
        location: str = self.__location.alpha_2 if self.__location else ""
        return f"{self.PREFIX}/attachment?location={location.lower()}"

    def load(self, path: str) -> bool:
        if not os.path.isfile(path):
            return False
        self.clear()
        for line in sorted(csv.DictReader(open(path)),
                           key=lambda x: int(x["rank"])):
            self.append(line["domain"])
        return True

    def download(self, path: str) -> bool:
        filepath: Optional[str] = download(url=self.url, path=path)
        status: str = "success" if isinstance(filepath, str) else "failed"
        commands().logger.debug(f"download {self.url} {status}")
        return self.load(filepath) if isinstance(filepath, str) else False
