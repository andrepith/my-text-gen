from fastapi import FastAPI
from app.api import endpoints

app = FastAPI(title="TinyLlama Chat API")

app.include_router(endpoints.router, prefix="/api")
