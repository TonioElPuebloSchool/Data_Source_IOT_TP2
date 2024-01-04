from fastapi import APIRouter, HTTPException
from src.services.data import download_dataset, load_iris_dataset, process_data, split_train_test, train_model, predict_model
from src.services.firestore import FirestoreClient
from sklearn.ensemble import RandomForestClassifier
import joblib


from fastapi import FastAPI

app = FastAPI()
firestore_client = FirestoreClient()

def update_firestore(key, new_value):
    firestore_client.update('parameters', key, new_value)
    
def add_param_firestore(new_value):
    firestore_client.add('parameters', new_value)

def train_model_with_firestore(key):
    df = load_iris_dataset()
    firestore_clien = FirestoreClient()
    X = df.drop(['Species', 'Id'], axis=1)
    y = df['Species']
    
    params = firestore_clien.get('parameters', key)
    X = df.drop(['Species', 'Id'], axis=1)
    y = df['Species']
    model = RandomForestClassifier(**params)
    model.fit(X, y)
    joblib.dump(model, 'services/epf-flower-data-science/src/models/model_param.pkl')
    
def predict_model_with_firestore(SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm):
    model = joblib.load('services/epf-flower-data-science/src/models/model_param.pkl')
    prediction = model.predict([[SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm]])
    return prediction[0]



    
    
    

