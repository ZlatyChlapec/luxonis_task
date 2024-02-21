import scrapy
from dependency_injector import wiring as wr

from ..app import containers as cnt, models as ml, services as svc


class StoragePipeline(object):

    @staticmethod
    @wr.inject
    def process_item(
        item: scrapy.Item,
        _spider: scrapy.Spider,
        service: svc.Advert = wr.Provide[cnt.BaseContainer.advert_srv],
    ) -> scrapy.Item:
        if isinstance(item, ml.Advert):
            service.add(item)
        return item
