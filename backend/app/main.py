from fastapi import FastAPI
#from starlette.middleware.cors import CORSMiddleware

#from app.api.api_v1.api import api_router
#from app.core.config import settings

app = FastAPI(
    docs_url="/api",
    redoc_url=None
)