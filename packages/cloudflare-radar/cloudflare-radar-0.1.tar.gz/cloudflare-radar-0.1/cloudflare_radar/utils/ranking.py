# coding:utf-8

from typing import Optional

from pycountry.db import Country
from xarg import commands

from .request import download


class domain_ranking():
    PREFIX = "http://radar.cloudflare.com/charts/TopDomainsTable"

    def __init__(self, location: Optional[Country] = None):
        self.__location: Optional[Country] = location

    @property
    def location(self) -> str:
        return self.__location.name if self.__location else "Worldwide"

    @property
    def url(self) -> str:
        location: str = self.__location.alpha_2 if self.__location else ""
        return f"{self.PREFIX}/attachment?location={location.lower()}"

    def download(self, path: str) -> bool:
        filepath: Optional[str] = download(url=self.url, path=path)
        success: bool = True if isinstance(filepath, str) else False
        status: str = "success" if success else "failed"
        commands().logger.info(f"download {self.url} {status}")
        return success
