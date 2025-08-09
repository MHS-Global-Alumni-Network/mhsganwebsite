from django.db import models
from django.conf import settings


# Create your models here.
class Chapter(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    chair = models.TextField(max_length=255,
                             null=True)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   on_delete=models.SET_NULL,
                                   null=True,
                                   blank=True)

    def __str__(self):
        return self.name
