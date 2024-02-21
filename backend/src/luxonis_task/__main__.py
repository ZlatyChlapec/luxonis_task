import logging

import uvicorn

from .api import base as abase
from .scrp import base as sbase

logging.basicConfig(level=logging.INFO)

sbase.populate_db()
uvicorn.run(abase.create_app(), reload=True)
