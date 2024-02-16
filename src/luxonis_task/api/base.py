import os
import fastapi as fa

from ..app import containers as cnt
from . import endpoints


def create_app() -> fa.FastAPI:
    container = cnt.BaseContainer()
    container.config.db.url.from_value(
        f"postgresql+psycopg://postgres:{os.getenv("POSTGRES_PASSWORD")}@db/postgres"
    )

    app = fa.FastAPI()
    app.container = container
    app.include_router(endpoints.router)
    return app
