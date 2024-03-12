from fastapi import APIRouter
from starlette.responses import RedirectResponse

router = APIRouter()

# home page
@router.get("/", name="Home Page", description="API Documentation Page.")
async def home_page():
    """API Documentation Page."""
    return RedirectResponse(url="/docs")