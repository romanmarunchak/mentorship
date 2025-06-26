from config import settings
from services.api_client import ApiClient
from models.object_model import ObjectModel


class ObjectService:
    def __init__(self):
        self.client = ApiClient(settings.BASE_API_URL)

    def create_object(self, payload: ObjectModel) -> ObjectModel:
        """
        Creates a new object by sending a typed payload to the API.
        """
        response = self.client.objects.create(payload.to_dict())
        return ObjectModel(**response)

    def get_object(self, object_id: str) -> ObjectModel:
        """
        Retrieves an object by its ID and parses it into ObjectModel.
        """
        response = self.client.objects.get(object_id)
        return ObjectModel(**response)

    # TODO: implement update_object(self, object_id: str, payload: ObjectPayload)
    # TODO: implement patch_object(self, object_id: str, patch_data: dict)
    # TODO: implement delete_object(self, object_id: str)