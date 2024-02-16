import scrapy
from dependency_injector import wiring as wr

from ..app import containers as cnt, services as svc
from . import items


class StoragePipeline(object):

    @staticmethod
    @wr.inject
    def process_item(
        item: scrapy.Item,
        _spider: scrapy.Spider,
        service: svc.Advert = wr.Provide[cnt.BaseContainer.advert_srv],
    ) -> scrapy.Item:
        if isinstance(item, items.Advert):
            service.add(item)
        return item
