import contextlib
from collections import abc

from sqlalchemy import orm

from . import models


class Advert:
    def __init__(
        self, session_factory: contextlib.AbstractContextManager[orm.Session]
    ) -> None:
        self._session_factory = session_factory

    def add(self, advert: models.Advert) -> int:
        with self._session_factory() as session:
            session.add(advert)
            session.commit()
            session.refresh(advert)
            return advert.id

    def get_all(self) -> abc.Iterator[models.Advert]: ...

    def get_last(self) -> models.Advert:
        with self._session_factory() as session:
            return (
                session.query(models.Advert).order_by(models.Advert.id.desc()).first()
            )
