import pytest
from models.object_model import ObjectModel
from services.object_service import ObjectService


@pytest.fixture
def created_object() -> ObjectModel:
    """
    Creates an object via ObjectService and deletes it after the test.

    The test is responsible for initializing ObjectService itself.
    """
    client = ObjectService()
    payload = ObjectModel(
        name="Router",
        data={
            "brand": "TP-Link",
            "specs": {"frequency": "5GHz"}
        }
    )
    created = client.create_object(payload)
    yield created
    client.client.objects.delete(created.id)