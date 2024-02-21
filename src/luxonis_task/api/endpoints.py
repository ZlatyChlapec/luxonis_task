import fastapi as fa
from dependency_injector import wiring as wr
from fastapi import responses as far
from sqlalchemy import exc as sexc

from ..app import containers as cnt, models as ml, services as svc

router = fa.APIRouter()


@router.get("/", response_class=far.HTMLResponse)
@wr.inject
def get_adverts(
    service: svc.Advert = fa.Depends(wr.Provide[cnt.BaseContainer.advert_srv]),
) -> str:
    code = ""
    total = 0

    try:
        for advert in service.get_all():
            total += 1
            code += f"""
            <div>
                <ul>
                    <li class="title"><a href="{advert.url}">{advert.title}</a></li>
                    <li><img src="{advert.images[0]}"></li>
                </ul>
            </div>
            """
    except sexc.ProgrammingError:
        raise fa.HTTPException(status_code=503, detail="Missing data")
    return f"""
    <html>
        <head>
            <title>List of {total} adverts</title>
        <style>
            a {{
                color: lightblue;
            }}
            body {{
                background-color: black;
                color: white;
            }}
            img {{
                height: 500px;
                width: 400px;
            }}
            ul {{
                list-style-type: none;
            }}
            .grid {{
                display: grid;
                grid-template-columns: repeat(auto-fill, minmax(400px, 1fr));
                grid-column-gap: 0px;
                grid-row-gap: 0px;
            }}
            .title {{
                margin: 0 0 10px 0;
            }}
        </style>
        </head>
        <body>
            <div class="grid">
                {code}
            </div>
        </body>
    </html>
    """


@router.get("/api/adverts/v1", response_model=None)
@wr.inject
def api_get_adverts(
        service: svc.Advert = fa.Depends(wr.Provide[cnt.BaseContainer.advert_srv]),
) -> list[ml.Advert]:
    try:
        return list(service.get_all())
    except sexc.ProgrammingError:
        raise fa.HTTPException(status_code=503, detail="Missing data")
