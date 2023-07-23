import logging

from django.test import TestCase
from mock_server.models import Response

logger = logging.getLogger('test_logger')


class ResponseManagerTestCase(TestCase):
    def setUp(self):
        self.response_data = [
            {
                "id": 1,
                "title": "user_data",
                "content": '{"username": "JohnDoe123", "email": "johndoe123@example.com", "age": 28, "is_active": true}',
            },
        ]

        for response_info in self.response_data:
            Response.objects.create(**response_info)

    def test_get_object_success(self):
        response_id = 1
        response_object = Response.objects.get_object(id=response_id)
        self.assertIsInstance(response_object, Response)
        self.assertEqual(response_object.id, response_id)

    def test_get_object_not_found(self):
        response_id = 999
        response_object = Response.objects.get_object(id=response_id)
        self.assertFalse(response_object)

    def test_get_object_exception(self):
        response_id = "invalid_id"
        response_object = Response.objects.get_object(id=response_id)
        self.assertIsNone(response_object)
