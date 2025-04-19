from django import forms
from django.forms import ModelForm
from .models import Event

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'location', 'date', 'time']
        widgets = {
            'date': DateInput(),
            'time': TimeInput(),
            }
