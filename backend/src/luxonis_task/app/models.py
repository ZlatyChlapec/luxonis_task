import dataclasses as dc
import datetime as dt


@dc.dataclass(slots=True)
class Advert:
    images: [str]
    price: int
    title: str
    url: str
    inserted: dt.datetime | None = None
