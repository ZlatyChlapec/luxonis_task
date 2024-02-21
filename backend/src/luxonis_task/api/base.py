import os
import fastapi as fa
from fastapi.middleware import cors as fac

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
    app.add_middleware(
        fac.CORSMiddleware,
        allow_origins=[
            "http://127.0.0.1:5173",
            "http://localhost:5173",
        ],
    )
    return app
