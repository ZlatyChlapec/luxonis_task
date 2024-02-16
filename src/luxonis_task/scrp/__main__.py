import logging

from . import base

logging.basicConfig(level=logging.INFO)

base.populate_db()
