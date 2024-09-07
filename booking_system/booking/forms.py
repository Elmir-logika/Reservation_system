# 

from django import forms
from .models import Booking, Room

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['room', 'start_date', 'end_date']

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'capacity', 'price', 'description', 'is_available']
