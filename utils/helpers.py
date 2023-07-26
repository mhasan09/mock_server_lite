import json
import logging
from django.conf import settings


def get_logger(name):
    return logging.getLogger(f"{settings.LOGGER_ROOT_NAME}.{name}")


logger = get_logger(__name__)


def parse_all_responses_data(data):
    try:
        return [
            {
                "id": item.id,
                "title": item.title,
                "content": json.loads(item.content),
                "created_at": item.created_at.strftime("%Y-%m-%d %H:%M:%S.%f"),
            }
            for item in data
        ]

    except Exception as e:
        logger.debug({"error": repr(e)})
        return None


def parse_single_response_data(obj):
    try:
        return {
            "id": obj.id,
            "title": obj.title,
            "content": json.loads(obj.content),
            "created_at": obj.created_at.strftime("%Y-%m-%d %H:%M:%S.%f"),
        }

    except Exception as e:
        logger.warning({"error": repr(e)})
        return None
