from django.http import JsonResponse
from mock_server.models import Response
from utils.helpers import (
    parse_single_response_data,
    parse_all_responses_data, get_logger,
)

logger = get_logger(__name__)


def get_all_responses(request):
    posts = Response.objects.get_all_objects()
    data = parse_all_responses_data(posts)
    logger.debug({"data": data})
    return JsonResponse(data)


def get_single_response(request, response_id):
    response_obj = Response.objects.get_object(response_id=response_id)
    data = parse_single_response_data(response_obj)
    logger.debug({"data": data})
    return JsonResponse(data)
