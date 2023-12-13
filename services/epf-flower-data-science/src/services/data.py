import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi
from src.schemas.message import MessageResponse
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import json

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

def split_train_test(test_size=0.2, random_state=42):
    df = pd.read_csv('data/Iris.csv')
    train_df, test_df = train_test_split(df, test_size=test_size, random_state=random_state)
    return train_df.to_dict(orient='records'), test_df.to_dict(orient='records')