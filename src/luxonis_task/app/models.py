import datetime as dt

import sqlalchemy as sa
from sqlalchemy import orm


class Base(orm.DeclarativeBase):
    pass


class Advert(Base):
    __tablename__ = "advert"

    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)
    images: orm.Mapped[str]
    inserted: orm.Mapped[dt.datetime] = orm.mapped_column(insert_default=sa.func.now())
    price: orm.Mapped[int]
    title: orm.Mapped[str]
    url: orm.Mapped[str]

    def __repr__(self) -> str:
        return (
            f"Advert(id={self.id!r}, "
            f"images={self.images!r}, "
            f"price={self.price!r}, "
            f"title={self.title!r}, "
            f"url={self.url!r})"
        )
