from django import forms

# Form for create a New Reservation
class MakeReservation(forms.Form):
    client = forms.TextInput()
    persons = forms.IntegerField()
    entrance = forms.DateField()
    exit = forms.DateField()
    payment = forms.DecimalField(max_digits=6, decimal_places=3)