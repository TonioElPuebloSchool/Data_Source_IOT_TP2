"""API Router for Fast API."""

# Import the necessary modules
from fastapi import APIRouter
from src.api.routes import hello, data, parameters

# Create a new router
router = APIRouter()

# Include the routers from the 'hello', 'data', and 'parameters' modules
# The 'tags' argument is used to group the routes in the API documentation
router.include_router(hello.router, tags=["Hello"])
router.include_router(data.router, tags=["Data"])
router.include_router(parameters.router, tags=["Custom_Parameters"])