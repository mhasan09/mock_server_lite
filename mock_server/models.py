from django.core.exceptions import ObjectDoesNotExist
from django.db import models

from utils.helpers import get_logger

logger = get_logger(__name__)


class ResponseManager(models.Manager):
    def get_object(self, id):
        try:
            return self.get(id=id)

        except ObjectDoesNotExist as e:
            logger.debug({"payload": id, "db_exception_error": repr(e)})
            return False

        except Exception as e:
            logger.debug({"payload": id, "db_exception_error": repr(e)})
            return None

    def get_all_objects(self):
        return self.all()


class Response(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    objects = ResponseManager()

    def __str__(self):
        return self.title
