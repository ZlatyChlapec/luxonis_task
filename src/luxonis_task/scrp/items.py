import dataclasses as dc
import datetime as dt


@dc.dataclass(slots=True)
class Advert:
    images: [str]
    inserted: dt.datetime | None
    price: int
    title: str
    url: str
