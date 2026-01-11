from fastapi import FastAPI
from app.database.session import engine, Base
from app.database import models

app = FastAPI()


@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.get("/")
def root():
    return {"status": "mini-bank is running"}
