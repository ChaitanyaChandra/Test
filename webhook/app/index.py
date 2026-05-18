import os
from fastapi import FastAPI
from routers import validate_rewrite
import logging


if os.getenv("DEBUG", "false").lower() == "true":
    logging.root.setLevel(logging.DEBUG)

app = FastAPI()

app.include_router(validate_rewrite.router)

app.get("/health")
def health():
    return "200 - OK"