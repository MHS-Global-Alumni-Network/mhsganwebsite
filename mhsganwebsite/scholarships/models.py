from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Scholarship(models.Model):
    title = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    scholarship_details = models.TextField()
    deadline = models.DateField(null=True, blank=True)
    contact_name = models.CharField(null=False, max_length=255)
    contact_phone = PhoneNumberField()
    contact_email = models.EmailField()
    application_link = models.URLField(max_length=500)

    def __str__(self):
        return self.title
