from django import forms

class Register(forms.Form):
    first_name = forms.TextInput()
    last_name = forms.TextInput()
    email = forms.EmailField()
    phone = forms.NumberInput()
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()


class Login(forms.Form):
    email = forms.EmailInput()
    password1 = forms.PasswordInput()