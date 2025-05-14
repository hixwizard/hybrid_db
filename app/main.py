from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.db.postgres.session import engine
from app.db.postgres.base import base
from app.api.v1.endpoints.book import router as book_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(base.metadata.create_all)
    yield
    await engine.dispose()

app = FastAPI(lifespan=lifespan)
app.include_router(book_router, prefix="/books", tags=["books"])


@app.get("/health")
async def health_check():
    return {"status": "ok"}
