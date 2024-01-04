import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi
from src.schemas.message import MessageResponse
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import json
import joblib

def download_dataset():
    """
    Download the Iris dataset from Kaggle.

    Returns:
        None
    """
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files('uciml/iris', path='data', unzip=True)

def load_iris_dataset():
    """
    Load the Iris dataset from a CSV file.

    Returns:
        list of dict: The loaded Iris dataset.
    """
    df = pd.read_csv('data/Iris.csv')
    return df.to_dict(orient='records')

def process_data():
    """
    Process the Iris dataset.

    Returns:
        list of dict: The processed Iris dataset.
    """
    df = pd.read_csv('data/Iris.csv')
    scaler = StandardScaler()
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
    df[numeric_columns] = scaler.fit_transform(df[numeric_columns])
    return df.to_dict(orient='records')


def split_train_test(test_size=0.2, random_state=42):
    """
    Split the Iris dataset into training and test sets.

    Args:
        test_size (float): The proportion of the dataset to include in the test split.
        random_state (int): The seed used by the random number generator.

    Returns:
        tuple: The training and test sets.
    """
    df = pd.read_csv('data/Iris.csv')
    train_df, test_df = train_test_split(df, test_size=test_size, random_state=random_state)
    train_df.to_csv('data/train.csv', index=False)
    test_df.to_csv('data/test.csv', index=False)
    return train_df.to_dict(orient='records'), test_df.to_dict(orient='records')

def train_model():
    """
    Train a Random Forest model on the Iris dataset.

    Returns:
        None
    """
    df = pd.read_csv('data/train.csv')
    X = df.drop(['Species', 'Id'], axis=1)
    y = df['Species']
    with open('services/epf-flower-data-science/src/config/model_parameters.json') as fh:
        params = json.load(fh)
    model = RandomForestClassifier(**params)
    model.fit(X, y)
    joblib.dump(model, 'services/epf-flower-data-science/src/models/model.pkl')
    
def predict_model(SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm):
    """
    Predict the Iris species using a trained model.

    Args:
        SepalLengthCm (float): The sepal length in cm.
        SepalWidthCm (float): The sepal width in cm.
        PetalLengthCm (float): The petal length in cm.
        PetalWidthCm (float): The petal width in cm.

    Returns:
        str: The predicted Iris species.
    """
    model = joblib.load('services/epf-flower-data-science/src/models/model.pkl')
    prediction = model.predict([[SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm]])
    return prediction[0]