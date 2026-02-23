from django import forms
from .models import Subscriber


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['first_name',
                  'last_name',
                  'email',
                  'is_alumni',
                  'year_group']

    def clean(self):
        cleaned_data = super().clean()
        is_alumni = cleaned_data.get('is_alumni')
        year_group = cleaned_data.get('year_group')

        if is_alumni and not year_group:
            raise forms.ValidationError("Graduation year is required for alumni.")

        return cleaned_data
