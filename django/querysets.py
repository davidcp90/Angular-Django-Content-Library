from django.db import models
from datetime import datetime


class CourseQuerySet(models.QuerySet):
    """

        Queryset para model Course
    """
    def get_list(self):
        return self.filter().first()

class CourseResourceQuerySet(models.QuerySet):
    """
        Queryset para model Course Resource
    """
    def get_or_none(self, id):
        try:
            return self.get(id=id)
        except Exception:
            return None

class CourseStudentResourceQuerySet(models.QuerySet):
    """
        Queryset para modelo CourseStudentResource
    """
    def get_or_none(self, id):
        """
            Retorna model si existe, si no retorna None
        """
        try:
            return self.get(id=id)
        except Exception:
            return None