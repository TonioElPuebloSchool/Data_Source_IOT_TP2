import google.auth
from google.cloud import firestore


class FirestoreClient:
    """Wrapper around a database"""

    client: firestore.Client

    def __init__(self) -> None:
        """Init the client."""
        
        self.client = firestore.Client.from_service_account_json('services/epf-flower-data-science/src/config/datasourceapi-b7fac-firebase-adminsdk-53gb4-757878c47f.json')

    def get(self, collection_name: str, document_id: str) -> dict:
        """Find one document by ID.
        Args:
            collection_name: The collection name
            document_id: The document id
        Return:
            Document value.
        """
        doc = self.client.collection(collection_name).document(document_id).get()
        if doc.exists:
            return doc.to_dict()
        raise FileExistsError(
            f"No document found at {collection_name} with the id {document_id}"
        )
        
    def update(self, collection_name: str, document_id: str, data: dict) -> None:
        """Update a document by ID.
        Args:
            collection_name: The collection name
            document_id: The document id
            data: The data to update
        """
        self.client.collection(collection_name).document(document_id).update(data)
        
    def add(self, collection_name: str, data: dict) -> None:
        """Add a document to a collection.
        Args:
            collection_name: The collection name
            data: The data to add
        """
        self.client.collection(collection_name).add(data)