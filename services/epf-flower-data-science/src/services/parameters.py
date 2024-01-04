from fastapi import APIRouter, HTTPException
from src.services.data import download_dataset, load_iris_dataset, process_data, split_train_test, train_model, predict_model
from src.services.firestore import FirestoreClient
from sklearn.ensemble import RandomForestClassifier
import joblib
import pandas as pd

from fastapi import FastAPI

app = FastAPI()
firestore_client = FirestoreClient()

def update_firestore(key: str, new_value: dict):
    """
    Update a document in Firestore with a new value.

    Args:
        key (str): The ID of the document to update.
        new_value (dict): The new value to set the document to.
    """
    firestore_client.update('parameters', key, new_value)
    
def add_param_firestore(new_value):
    """
    Add a new document to Firestore.

    Args:
        new_value (dict): The value of the new document to add.
    """
    firestore_client.add('parameters', new_value)

def train_model_with_firestore(key: str):
    """
    Train a model with parameters from Firestore.

    Args:
        key (str): The ID of the document containing the parameters to use for training.
    """
    # Load the training data
    df = pd.read_csv('data/train.csv')
    # Initialize a Firestore client
    firestore_client = FirestoreClient()
    
    # Prepare the features and target variable
    X = df.drop(['Species', 'Id'], axis=1)
    y = df['Species']

    # Get the parameters for the model from Firestore
    params = firestore_client.get('parameters', key)
    # Train a Random Forest Classifier with the fetched parameters
    model = RandomForestClassifier(**params)
    model.fit(X, y)

    # Save the trained model
    joblib.dump(model, 'services/epf-flower-data-science/src/models/model_param.pkl')
    
def predict_model_with_firestore(SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm):
    """
    Predict a class using a model and parameters from Firestore.

    Args:
        SepalLengthCm (float): The sepal length in cm.
        SepalWidthCm (float): The sepal width in cm.
        PetalLengthCm (float): The petal length in cm.
        PetalWidthCm (float): The petal width in cm.

    Returns:
        str: The predicted Iris species.
    """
    # Load the trained model
    model = joblib.load('services/epf-flower-data-science/src/models/model_param.pkl')
    # Make a prediction using the model
    prediction = model.predict([[SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm]])
    
    # Return the predicted class
    return prediction[0]