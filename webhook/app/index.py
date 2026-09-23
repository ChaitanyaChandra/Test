import os
from fastapi import FastAPI
from app.routers import validate_rewrite, requests_limits
import logging


if os.getenv("DEBUG", "true").lower()  == "true":
    logging.root.setLevel(logging.DEBUG)

app = FastAPI()

app.include_router(validate_rewrite.router)
app.include_router(requests_limits.router)

app.get("/health")
def health():
    return "200 - OK"