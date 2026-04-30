from django import forms
from .models import Reservation

# Form for create a New Reservation
class MakeReservation(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = [
            "client",
            "cabin",
            "persons",
            "entrance",
            "exit",
            "payment",
        ]