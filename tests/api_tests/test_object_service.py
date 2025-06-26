
class TestObjectCRUD:

    def test_create_object(self, created_object):

        assert created_object.id
        assert created_object.name == "Router"
        assert created_object.data["brand"] == "TP-Link"

    # TODO: test_update_object
    # TODO: test_patch_object
    # TODO: test_delete_object
