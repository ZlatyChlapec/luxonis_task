import contextlib as ctx
import logging
from collections import abc

import sqlalchemy as sal
from sqlalchemy import exc, orm
from sqlalchemy.ext import declarative as dec

from . import models

log = logging.getLogger(__name__)
Base = dec.declarative_base()


class Database:
    def __init__(self, db_url: str) -> None:
        self._engine = sal.create_engine(db_url, echo=True)
        self._session_factory = orm.scoped_session(
            orm.sessionmaker(
                autoflush=False,
                bind=self._engine,
            )
        )

    def create_database(self) -> None:
        models.Base.metadata.create_all(self._engine)

    def drop_database(self) -> None:
        models.Base.metadata.drop_all(self._engine)

    @ctx.contextmanager
    def session(self) -> abc.Iterator[orm.Session]:
        session = self._session_factory()
        try:
            yield session
        except exc.SQLAlchemyError:
            log.exception("session.rollback")
            session.rollback()
            raise
        finally:
            session.close()
