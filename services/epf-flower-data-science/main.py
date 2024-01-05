import uvicorn

from src.app import get_application

app = get_application()

if __name__ == "__main__":
    uvicorn.run("main:app", port=8080, reload=True)
