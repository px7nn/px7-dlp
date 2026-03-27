from routes.search import search_yt
from routes.stream import get_stream_url
from fastapi import FastAPI

app = FastAPI(docs_url=None, redoc_url=None)

@app.get("/")
def home():
    return {"status": "px7-dlp running"}

@app.get("/search")
def search(query: str, postfix: str | None = None, limit: int | None = None):
    result = search_yt(query, postfix, limit)
    if not result:
        return {"error": "No results found"}
    return result

@app.get("/stream")
def stream(url: str):
    stream_url = get_stream_url(url)
    if not stream_url:
        return {"error": "Stream not available"}
    return {"stream_url": stream_url}
