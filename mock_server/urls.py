from django.urls import path

from mock_server.views import get_all_responses

urlpatterns = [
    path("/get-all-responses", get_all_responses, name="get-all-responses"),
    path("/get/<int:id>", get_all_responses, name="get-all-responses"),
]
