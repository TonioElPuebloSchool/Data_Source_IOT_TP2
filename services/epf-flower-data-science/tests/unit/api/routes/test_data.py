import pytest
from fastapi.testclient import TestClient
from unittest.mock import Mock, patch
import pandas as pd
import src.services.data as data
from sklearn.preprocessing import StandardScaler

class TestDataRoutes:
    @pytest.fixture
    def client(self) -> TestClient:
        """
        Test client for integration tests
        """
        from main import get_application

        app = get_application()

        client = TestClient(app, base_url="http://testserver")

        return client

    @patch('pandas.read_csv') 
    def test_load_iris_dataset(self, mock_read_csv, client):
        mock_read_csv.return_value = pd.DataFrame({
            "Id": [1, 2],
            "SepalLengthCm": [5.1, 4.9],
            "SepalWidthCm": [3.5, 3],
            "PetalLengthCm": [1.4, 1.4],
            "PetalWidthCm": [0.2, 0.2],
            "Species": ["Iris-setosa", "Iris-setosa"]
        })
        response = client.get("/loading_dataset")
        assert response.status_code == 200
        assert response.json()[:2] == [
            {
                "Id": 1,
                "SepalLengthCm": 5.1,
                "SepalWidthCm": 3.5,
                "PetalLengthCm": 1.4,
                "PetalWidthCm": 0.2,
                "Species": "Iris-setosa"
            },
            {
                "Id": 2,
                "SepalLengthCm": 4.9,
                "SepalWidthCm": 3,
                "PetalLengthCm": 1.4,
                "PetalWidthCm": 0.2,
                "Species": "Iris-setosa"
            }
        ]
    
    @patch('pandas.read_csv')
    def test_process_data(self, mock_read_csv, client):
        df = pd.DataFrame({
            "Id": [1, 2],
            "SepalLengthCm": [5.1, 4.9],
            "SepalWidthCm": [3.5, 3.0],
            "PetalLengthCm": [1.4, 1.4],
            "PetalWidthCm": [0.2, 0.2],
            "Species": ["Iris-setosa", "Iris-setosa"]
        })
        scaler = StandardScaler()
        numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
        df[numeric_columns] = scaler.fit_transform(df[numeric_columns])
        mock_read_csv.return_value = df
        response = client.get("/process_data")
        assert response.status_code == 200
        assert response.json()[:2] == df[:2].to_dict(orient='records')
        
    @patch('joblib.load')
    def test_predict_model(self, mock_load, client):
        mock_model = mock_load.return_value
        mock_model.predict.return_value = ['Iris-virginica']
        response = client.get("/predict_model", params={"SepalLengthCm": 4, "SepalWidthCm": 4, "PetalLengthCm": 4, "PetalWidthCm": 4})
        assert response.status_code == 200
        assert response.json() == 'Iris-virginica'