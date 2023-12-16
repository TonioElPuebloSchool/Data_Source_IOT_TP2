import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi
from src.schemas.message import MessageResponse
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import json
import joblib

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
    train_df.to_csv('data/train.csv', index=False)
    test_df.to_csv('data/test.csv', index=False)
    return train_df.to_dict(orient='records'), test_df.to_dict(orient='records')

def train_model():
    df = pd.read_csv('data/train.csv')
    X = df.drop('Species', axis=1)
    y = df['Species']
    with open('services/epf-flower-data-science/src/config/model_parameters.json') as fh:
        params = json.load(fh)
    model = RandomForestClassifier(**params)
    model.fit(X, y)
    joblib.dump(model, 'services/epf-flower-data-science/src/models/model.pkl')
    
