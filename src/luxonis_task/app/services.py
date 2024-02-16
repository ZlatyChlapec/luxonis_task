from ..scrp import items
from . import models, repositories as repo


class Advert:
    def __init__(self, advert_repo: repo.Advert) -> None:
        self._repo = advert_repo

    def add(self, advert: items.Advert) -> None:
        self._repo.add(
            models.Advert(
                images=";".join(advert.images),
                price=advert.price,
                title=advert.title,
                url=advert.url,
            )
        )

    def get_all(self): ...

    def get_last(self) -> items.Advert | None:
        advert = self._repo.get_last()
        if not advert:
            return None
        return items.Advert(
            advert.images.split(";"),
            advert.inserted,
            advert.price,
            advert.title,
            advert.url,
        )
