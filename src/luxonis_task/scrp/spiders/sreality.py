import json
import logging
import re
import time
from collections import abc
from typing import *

import scrapy
import scrapy.http as s_http

from ...app import models as ml
from .. import pipelines

log = logging.getLogger(__name__)


class SrealitySpider(scrapy.Spider):
    name = "sreality"
    custom_settings = {"ITEM_PIPELINES": {pipelines.StoragePipeline: 100}}
    start_urls = [
        f"https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1"
        f"&category_type_cb=1&per_page=60&tms={time.time_ns() // 1_000_000}",
    ]

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.pages_crawled = 0

    def parse(
        self, response: s_http.Response, **kwargs: Any
    ) -> abc.Generator[ml.Advert]:
        data = json.loads(response.body)
        for estate in data["_embedded"]["estates"]:
            yield ml.Advert(
                images=[
                    SrealitySpider._get_img_url(image["href"])
                    for image in estate["_links"]["images"]
                ],
                # price has incorrect value
                price=estate["price"],
                title=estate["name"],
                url=SrealitySpider._get_url(
                    estate["hash_id"],
                    estate["seo"]["locality"],
                    estate["name"],
                ),
            )
        if self.pages_crawled < 8:
            self.pages_crawled += 1
            per_page = 60
            if self.pages_crawled == 8:
                per_page = 20
            yield response.follow(
                url=f"/api/cs/v2/estates?category_main_cb=1&category_type_cb=1"
                f"&page={self.pages_crawled + 1}&per_page={per_page}"
                f"&tms={time.time_ns() // 1_000_000}",
                callback=self.parse,
            )

    @staticmethod
    def _get_img_url(url: str) -> str:
        """Make images bigger."""
        return (
            url.split("?")[0]
            + "?fl=res,1920,1080,1|wrm,/watermark/sreality.png,10|shr,,20|jpg,90"
        )

    @staticmethod
    def _get_url(hash_id: str, locality: str, name: str) -> str:
        """Create url for humans."""
        edge_cases = {
            "Prodej bytu 6 pokojů": "6-a-vice",
            "Prodej bytu atypické": "atypicky",
        }
        # example value "Prodej bytu 2+kk43\u00a0m\u00b2" desired result "2+kk"
        try:
            pattern = re.compile(r".*(\d\+(\d|kk)).*")
            size = pattern.search(name)[1]
        except TypeError:
            log.debug("_get_url.type_error", exc_info=True)
            size = edge_cases[name[:20]]

        return f"https://www.sreality.cz/detail/prodej/byt/{size}/{locality}/{hash_id}"
