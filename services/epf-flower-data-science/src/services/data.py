import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi
from src.schemas.message import MessageResponse
from sklearn.preprocessing import StandardScaler

def download_dataset():
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files('uciml/iris', path='data', unzip=True)

def load_iris_dataset():
    df = pd.read_csv('data/Iris.csv')
    return df.to_dict(orient='records')

def process_data():
    df = pd.read_csv('data/Iris.csv')
    scaler = StandardScaler()
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
    df[numeric_columns] = scaler.fit_transform(df[numeric_columns])
    return df.to_dict(orient='records')