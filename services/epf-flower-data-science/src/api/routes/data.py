from fastapi import APIRouter
from src.schemas.message import MessageResponse
#from src.services.data import download_dataset, load_iris_dataset, process_data, split_train_test
import src.services.data as data
router = APIRouter()

@router.get("/download_dataset")
def download():
    """
    Download the dataset.

    Returns:
        dict: The result of the download operation.
    """
    return data.download_dataset()

@router.get("/loading_dataset")
def loading():
    """
    Load the Iris dataset.

    Returns:
        DataFrame: The loaded Iris dataset.
    """
    return data.load_iris_dataset()

@router.get("/process_data")
def process():
    """
    Process the dataset.

    Returns:
        DataFrame: The processed dataset.
    """
    return data.process_data()

@router.get("/split_train_test")
def split(test_size: float = 0.2, random_state: int = 42):
    """
    Split the dataset into training and test sets.

    Args:
        test_size (float): The proportion of the dataset to include in the test split.
        random_state (int): The seed used by the random number generator.

    Returns:
        tuple: The training and test sets.
    """
    return data.split_train_test(test_size, random_state)

@router.get("/train_model")
def train():
    """
    Train the model.

    Returns:
        dict: The result of the training operation.
    """
    return data.train_model()

@router.get("/predict_model")
def predict(SepalLengthCm: float, SepalWidthCm: float, PetalLengthCm: float, PetalWidthCm: float):
    """
    Predict a class using the model.

    Args:
        SepalLengthCm (float): The sepal length in cm.
        SepalWidthCm (float): The sepal width in cm.
        PetalLengthCm (float): The petal length in cm.
        PetalWidthCm (float): The petal width in cm.

    Returns:
        dict: The prediction result.
    """
    return data.predict_model(SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm)
