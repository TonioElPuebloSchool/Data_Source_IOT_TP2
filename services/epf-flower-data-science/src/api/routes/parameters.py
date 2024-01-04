from fastapi import APIRouter
from src.services.parameters import update_firestore, add_param_firestore, train_model_with_firestore, predict_model_with_firestore
router = APIRouter()

@router.get("/update_firestore")
def update(key: str, new_value: float):
    update_firestore(key, new_value)
    return {"message": "Firestore updated"}

@router.get("/add_param_firestore")
def add(new_value: float):
    add_param_firestore(new_value)
    return {"message": "Firestore added"}

@router.get("/train_model_with_firestore")
def train(key: str):
    train_model_with_firestore(key = 'key')
    return {"message": "Model trained"}

@router.get("/predict_model_with_firestore")
def predict(SepalLengthCm: float, SepalWidthCm: float, PetalLengthCm: float, PetalWidthCm: float):
    return predict_model_with_firestore(SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm)

