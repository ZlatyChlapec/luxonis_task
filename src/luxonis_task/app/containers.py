from dependency_injector import containers as con, providers as prov

from . import database as db, repositories as repo, services as svc


class BaseContainer(con.DeclarativeContainer):
    config = prov.Configuration()
    db = prov.Singleton(db.Database, db_url=config.db.url)
    advert_repo = prov.Factory(repo.Advert, session_factory=db.provided.session)
    advert_srv = prov.Factory(svc.Advert, advert_repo=advert_repo)
    wiring_config = con.WiringConfiguration(modules=["..scrp.base", "..scrp.pipelines"])
