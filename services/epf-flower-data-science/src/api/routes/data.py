from fastapi import APIRouter
from src.schemas.message import MessageResponse
from src.services.data import download_dataset, load_iris_dataset, process_data


router = APIRouter()

@router.get("/download_dataset")
def download():
    return download_dataset()

@router.get("/loading_dataset")
def loading():
    return load_iris_dataset()

@router.get("/process_data")
def process():
    return process_data()

