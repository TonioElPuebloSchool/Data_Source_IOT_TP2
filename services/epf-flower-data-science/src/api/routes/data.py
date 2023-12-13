from fastapi import APIRouter
from src.schemas.message import MessageResponse
#from src.services.data import download_dataset, load_iris_dataset, process_data, split_train_test
import src.services.data as data
router = APIRouter()

@router.get("/download_dataset")
def download():
    return data.download_dataset()

@router.get("/loading_dataset")
def loading():
    return data.load_iris_dataset()

@router.get("/process_data")
def process():
    return data.process_data()

@router.get("/split_train_test")
def split(test_size: float = 0.2, random_state: int = 42):
    return data.split_train_test(test_size, random_state)

@router.get("/train_model")
def train():
    return data.train_model()