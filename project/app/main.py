import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api import ping, summaries
from app.db import init_db

log = logging.getLogger("uvicorn")


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    log.info("Starting up...")
    init_db(app)  # Initialize the database
    yield  # Application runs during this phase
    # Shutdown logic
    log.info("Shutting down...")


def create_application() -> FastAPI:
    application = FastAPI(lifespan=lifespan)
    application.include_router(ping.router)
    application.include_router(
        summaries.router, prefix="/summaries", tags=["summaries"]
    )

    return application


app = create_application()
