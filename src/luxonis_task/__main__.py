import logging

from scrapy import crawler as crw
from scrapy.utils import project as spj

from .scrp import spiders

logging.basicConfig(level=logging.INFO)

process = crw.CrawlerProcess(spj.get_project_settings())
process.crawl(spiders.SrealitySpider)
process.start()
