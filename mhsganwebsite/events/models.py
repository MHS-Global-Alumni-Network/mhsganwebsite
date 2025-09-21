from django.db import models
from django.conf import settings

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    event_details = models.TextField()
    event_contact_email = models.CharField(max_length=255)
    event_contact_phone = models.CharField(max_length=255, null=True, blank=True)
    event_contact_name = models.CharField(max_length=255)
    event_registration_link = models.CharField(null=True, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   on_delete=models.SET_NULL,
                                   null=True,
                                   blank=True)

    def __str__(self):
        return self.title
