import warnings

from fastapi import APIRouter, Depends

from app.config import Settings, get_settings

# Suppress DeprecationWarning
warnings.filterwarnings("ignore", category=DeprecationWarning)

router = APIRouter()


@router.get("/ping")
async def pong(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing,
    }
