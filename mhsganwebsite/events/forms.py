from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title',
                  'date',
                  'location',
                  'event_details',
                  'event_contact_email',
                  'event_contact_phone',
                  'event_contact_name',
                  'event_registration_link']
