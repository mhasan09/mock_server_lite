from django.urls import path

from mock_server.views import get_all_responses, get_single_response

urlpatterns = [
    path("all", get_all_responses, name="get-all-responses"),
    path("<int:id>", get_single_response, name="get-all-responses"),
]
