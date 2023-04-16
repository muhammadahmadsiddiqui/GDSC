from django import forms
from .models import Registration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['name', 'email', 'phone', 'roll_no', 'institute']
        labels = {
            'name': 'Your name',
            'email': 'Your email address',
            'phone': 'Your phone number',
            'roll_no': 'Your roll number',
            'institute': 'Your institute name',
        }
