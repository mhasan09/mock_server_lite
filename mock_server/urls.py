from django.urls import path

from mock_server.views import get_all_responses

urlpatterns = [
    path("all", get_all_responses, name="get-all-responses"),
    path("response/<int:id>", get_all_responses, name="get-all-responses"),
]
