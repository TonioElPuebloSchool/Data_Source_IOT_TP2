from fastapi import APIRouter
from src.services.parameters import update_firestore, add_param_firestore, train_model_with_firestore, predict_model_with_firestore
router = APIRouter()

@router.put("/update_firestore")
def update(key: str, new_value: dict):
    """
    Update a document in Firestore with a new value.

    Args:
        key (str): The ID of the document to update.
        new_value (dict): The new value to set the document to.

    Returns:
        dict: A message indicating the update was successful.
    """
    update_firestore(key, new_value)
    return {"message": "Firestore updated"}

@router.post("/add_param_firestore")
def add(new_value: dict):
    """
    Add a new document to Firestore.

    Args:
        new_value (dict): The value of the new document to add.

    Returns:
        dict: The result of the add operation.
    """
    result = add_param_firestore(new_value)
    #return {"message": "Firestore added"} 
    return result

@router.get("/train_model_with_firestore")
def train(key: str = "IekD8UZJBtzORWABaztJ"):
    """
    Train a model with parameters from Firestore.

    Args:
        key (str): The ID of the document containing the parameters to use for training.

    Returns:
        dict: A message indicating the model was trained successfully.
    """
    train_model_with_firestore(key)
    return {"message": "Model trained"}

@router.get("/predict_model_with_firestore")
def predict(SepalLengthCm: float, SepalWidthCm: float, PetalLengthCm: float, PetalWidthCm: float):
    """
    Predict a class using a model and parameters from Firestore.

    Args:
        SepalLengthCm (float): The sepal length in cm.
        SepalWidthCm (float): The sepal width in cm.
        PetalLengthCm (float): The petal length in cm.
        PetalWidthCm (float): The petal width in cm.

    Returns:
        dict: The prediction result.
    """
    return predict_model_with_firestore(SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm)

