from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl
from uuid import UUID, uuid4

app = FastAPI()


class BookmarkIn(BaseModel):
    title: str
    url: HttpUrl
    tags: list[str] = []


class BookmarkOut(BookmarkIn):
    id: UUID
    read: bool = False


bookmarks: dict[str, "BookmarkOut"] = {}


@app.post("/bookmarks")
async def create_bookmark(bookmark: BookmarkIn):
    bookmark_id = uuid4()
    bookmark_out = BookmarkOut(
        id=bookmark_id,
        title=bookmark.title,
        url=bookmark.url,
        tags=bookmark.tags,
        read=False,
    )

    bookmarks[str(bookmark_id)] = bookmark_out
    return bookmark_out


@app.get("/bookmarks")
async def get_bookmarks():
    return bookmarks
