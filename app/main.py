from fastapi import FastAPI, Depends
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert

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
