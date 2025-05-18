from pydantic import BaseModel, HttpUrl


class UrlIn(BaseModel):
    url: HttpUrl
