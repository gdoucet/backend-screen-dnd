from fastapi import FastAPI

app = FastAPI(
    docs_url="/api",
    redoc_url=None
)
