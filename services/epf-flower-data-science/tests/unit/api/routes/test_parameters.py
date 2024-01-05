import pytest
from fastapi.testclient import TestClient
from unittest.mock import Mock, patch

class TestParametersRoutes:
    @pytest.fixture
    def client(self) -> TestClient:
        """
        Test client for integration tests
        """
        from main import get_application

        app = get_application()

        client = TestClient(app, base_url="http://testserver")

        return client

    @patch('src.services.parameters.FirestoreClient')
    def test_update_firestore(self, mock_firestore_client, client):
        mock_firestore_client.update.return_value = None
        response = client.put("/update_firestore", params={"key": "IekD8UZJBtzORWABaztJ"}, json={"criterion": "gini","n_estimators": 100})
        assert response.status_code == 200
        assert response.json() == {"message": "Firestore updated"}

    @patch('src.services.parameters.FirestoreClient')
    def test_add_param_firestore(self, mock_firestore_client, client):
        mock_firestore_client.add.return_value = {"id": "test_id"}
        response = client.post("/add_param_firestore", json={"criterion": "gini", "n_estimators": 100})
        assert response.status_code == 200

    @patch('src.services.parameters.FirestoreClient')
    @patch('src.services.parameters.joblib.dump')
    def test_train_model_with_firestore(self, mock_dump, mock_firestore_client, client):
        mock_firestore_client.get.return_value = {"n_estimators": 100, "max_depth": None}
        response = client.get("/train_model_with_firestore", params={"key": "IekD8UZJBtzORWABaztJ"})
        assert response.status_code == 200
        assert response.json() == {"message": "Model trained"}

    @patch('src.services.parameters.FirestoreClient')
    @patch('src.services.parameters.joblib.load')
    def test_predict_model_with_firestore(self, mock_load, mock_firestore_client, client):
        mock_load.return_value.predict.return_value = ["Iris-versicolor"]
        response = client.get("/predict_model_with_firestore", params={"SepalLengthCm": 4, "SepalWidthCm": 4, "PetalLengthCm": 4, "PetalWidthCm": 4})
        assert response.status_code == 200
        assert response.json() == "Iris-versicolor"