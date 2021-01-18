from django import forms
import datetime
from .models import Hall
class AvailabilityForm(forms.Form):
    # room_category = forms.ModelChoiceField(
    #     queryset=RoomCategory.objects.all())
    # room_size=(
    #     ('Hall A','50'),
    #     ('Hall B','100'),
    #     ('Hall C','200'),
    #     ('Hall D','350'),
    #     ('Hall E','500'),
    #     ('Hall F','1000'),
    # )

    capacity=forms.IntegerField(required=True)
    check_in=forms.DateTimeField(required=True,input_formats=["%Y-%m-%dT%H:%M"], widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    check_out=forms.DateTimeField(required=True,input_formats=["%Y-%m-%dT%H:%M"], widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))