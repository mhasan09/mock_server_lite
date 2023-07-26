from django.http import JsonResponse
from mock_server.models import Response
from utils.helpers import (
    parse_single_response_data,
    parse_all_responses_data, get_logger,
)

logger = get_logger(__name__)


def get_all_responses(request):
    try:
        responses = Response.objects.get_all_objects()
        data = parse_all_responses_data(responses)
        logger.debug({"data": data})
        return JsonResponse(data, safe=False)

    except Exception as e:
        logger.error(f"An error occurred: {e}")
        return JsonResponse({"error": "An error occurred"}, status=500)


def get_single_response(request, id):
    try:
        response_obj = Response.objects.get_object(id=id)

        if response_obj is None:
            logger.warning(f"Response object with ID {id} not found.")
            return JsonResponse({"error": "Response not found"}, status=404)

        data = parse_single_response_data(obj=response_obj)
        logger.debug({"data": data})
        return JsonResponse(data, safe=False)

    except Exception as e:
        logger.error(f"An error occurred: {e}")
        return JsonResponse({"error": "An error occurred"}, status=500)
