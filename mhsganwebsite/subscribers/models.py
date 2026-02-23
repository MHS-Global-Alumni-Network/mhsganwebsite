from django.db import models
from django.core.exceptions import ValidationError

class Subscriber(models.Model):
    # Add your fields here
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    is_alumni = models.BooleanField(default=False, verbose_name="Are you an Alumnus?")
    year_group = models.IntegerField(null=True, blank=True, verbose_name="Graduation Year (Alumni only)")


    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})".strip()


    def clean(self):
        super().clean()
        if self.is_alumni and not self.year_group:
            raise ValidationError({
                'year_group': 'Graduation year is required for alumni.'
            })
