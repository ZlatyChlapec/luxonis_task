import contextlib
from collections import abc

from sqlalchemy import orm

from . import entities as et


class Advert:
    def __init__(
        self, session_factory: contextlib.AbstractContextManager[orm.Session]
    ) -> None:
        self._session_factory = session_factory

    def add(self, advert: et.Advert) -> int:
        with self._session_factory() as session:
            session.add(advert)
            session.commit()
            session.refresh(advert)
            return advert.id

    def delete_all(self) -> int:
        with self._session_factory() as session:
            return session.query(et.Advert).delete()

    def get_all(self) -> abc.Generator[et.Advert]:
        with self._session_factory() as session:
            return session.query(et.Advert).all()

    def get_last(self) -> et.Advert:
        with self._session_factory() as session:
            return (
                session.query(et.Advert).order_by(et.Advert.id.desc()).first()
            )
