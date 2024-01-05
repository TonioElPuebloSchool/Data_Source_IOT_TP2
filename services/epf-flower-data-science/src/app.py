from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse, JSONResponse
from starlette.middleware.cors import CORSMiddleware

from src.api.router import router


def get_application() -> FastAPI:
    application = FastAPI(
        title="epf-flower-data-science", 
        description="""Fast API""",
        version="1.0.0",
        redoc_url=None,
    )

    @application.get("/", include_in_schema=False)
    async def redirect_to_docs():
        return RedirectResponse(url="/docs")
    
    # the follwogin was created for the step 20 : error handling
    @application.exception_handler(HTTPException)
    async def http_exception_handler(request, exc):
        if exc.status_code == 404:
            return JSONResponse(
                status_code=404,
                content={"message": "Item not found"},
            )
        # You can add more custom responses for other status codes here
        return JSONResponse(
            status_code=500,
            content={"message": "An unexpected error has occurred."},
        )
    
    
    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.include_router(router)
    return application