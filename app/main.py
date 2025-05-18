from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import RedirectResponse
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, select

import secrets

from app.database.dependencies import get_db
from app.schemas import UrlIn
from app.config import BYTES_QUANTITY, HOME_PAGE
from app.database.models import URL


app = FastAPI()


@app.post("/")
async def create_short_url(db: Annotated[AsyncSession, Depends(get_db)], url: UrlIn):
    short_url = secrets.token_urlsafe(BYTES_QUANTITY)
    original_url = str(url.url)

    await db.execute(insert(URL).values(short_url=short_url, original_url=original_url))
    await db.commit()

    return {"short_url": HOME_PAGE + short_url}


@app.get(
    "/{short_url}",
    response_class=RedirectResponse,
    responses={301: {"description": "Redirect to original url"}},
)
async def redirect(db: Annotated[AsyncSession, Depends(get_db)], short_url: str):
    record = await db.scalar(select(URL).where(URL.short_url == short_url))

    if record is None:
        raise HTTPException(status_code=404, detail="This url does not exist!")

    return RedirectResponse(url=record.original_url)
