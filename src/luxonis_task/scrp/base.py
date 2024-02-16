import datetime as dt
import os

from dependency_injector import wiring as wr
from scrapy import crawler as crw
from scrapy.utils import project as spj

from ..app import containers as cnt, services as svc
from . import items, spiders


def populate_db() -> None:
    container = cnt.BaseContainer()
    container.config.db.url.from_value(
        f"postgresql+psycopg://postgres:{os.getenv("POSTGRES_PASSWORD")}@db/postgres"
    )

    database = container.db()
    database.create_database()

    last_advert = _get_last_advert()
    if not last_advert or last_advert.inserted < dt.datetime.now() - dt.timedelta(minutes=30):
        process = crw.CrawlerProcess(spj.get_project_settings())
        process.crawl(spiders.SrealitySpider)
        process.start()


def _get_last_advert(
        service: svc.Advert = wr.Provide[cnt.BaseContainer.advert_srv]
) -> items.Advert:
    return service.get_last()
