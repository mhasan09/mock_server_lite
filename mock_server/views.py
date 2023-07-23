from django.http import JsonResponse
from mock_server.models import Response
from utils.helpers import (
    parse_single_response_data,
    parse_all_responses_data, get_logger,
)

logger = get_logger(__name__)


def get_all_responses(request):
    responses = Response.objects.get_all_objects()
    data = parse_all_responses_data(responses)
    logger.debug({"data": data})
    return JsonResponse(data, safe=False)


def get_single_response(request, id):
    response_obj = Response.objects.get_object(id=id)
    data = parse_single_response_data(obj=response_obj)
    logger.debug({"data": data})
    return JsonResponse(data)
