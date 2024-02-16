import dataclasses


@dataclasses.dataclass(slots=True)
class Advert:
    images: [str]
    price: int
    title: str
    url: str
