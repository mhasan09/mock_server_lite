import json
import logging
from django.conf import settings


def get_logger(name):
    return logging.getLogger(f"{settings.LOGGER_ROOT_NAME}.{name}")


def parse_all_responses_data(data):
    return [
        {
            "id": item.id,
            "title": item.title,
            "content": json.loads(item.content),
            "created_at": item.created_at.strftime("%Y-%m-%d %H:%M:%S.%f"),
        }
        for item in data
    ]


def parse_single_response_data(obj):
    return {
            "id": obj.id,
            "title": obj.title,
            "content": json.loads(obj.content),
            "created_at": obj.created_at.strftime("%Y-%m-%d %H:%M:%S.%f"),
        }
