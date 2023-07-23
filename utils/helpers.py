import logging
from django.conf import settings


def get_logger(name):
    return logging.getLogger(f"{settings.LOGGER_ROOT_NAME}.{name}")


def parse_all_responses_data(data):
    return [
        {
            "id": post.get("id"),
            "title": post.get("title"),
            "content": post.get("content"),
            "created_at": post.get("created_at"),
        }
        for post in data.get("posts", [])
    ]


def parse_single_response_data(data):
    return {
        "id": data.get("id"),
        "title": data.get("title"),
        "content": data.get("content"),
        "created_at": data.get("created_at"),
    }
