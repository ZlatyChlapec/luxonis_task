import logging

import uvicorn

from . import base

logging.basicConfig(level=logging.INFO)

uvicorn.run(base.create_app(), reload=True)
