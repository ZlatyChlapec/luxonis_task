from collections import abc

from . import entities as et, models as ml, repositories as repo


class Advert:
    def __init__(self, advert_repo: repo.Advert) -> None:
        self._repo = advert_repo

    def add(self, advert: ml.Advert) -> None:
        self._repo.add(
            et.Advert(
                images=";".join(advert.images),
                price=advert.price,
                title=advert.title,
                url=advert.url,
            )
        )

    def delete_all(self) -> int:
        return self._repo.delete_all()

    def get_all(self) -> abc.Generator[ml.Advert]:
        for advert in self._repo.get_all():
            yield ml.Advert(
                advert.images.split(";"),
                advert.price,
                advert.title,
                advert.url,
                advert.inserted,
            )

    def get_last(self) -> ml.Advert | None:
        advert = self._repo.get_last()
        if not advert:
            return None
        return ml.Advert(
            advert.images.split(";"),
            advert.price,
            advert.title,
            advert.url,
            advert.inserted,
        )
