from django.db import models
from django.conf import settings


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   on_delete=models.SET_NULL,
                                   null=True,
                                   blank=True)
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
