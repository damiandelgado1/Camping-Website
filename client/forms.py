from django import forms


# Contact form for Contact to Site
class Contact(forms.Form):
    name = forms.TextInput()
    email = forms.EmailInput()
    phone = forms.NumberInput()


# Data by Resgiter account
class Register(forms.Form):
    first_name = forms.TextInput()
    last_name = forms.TextInput()
    email = forms.EmailField()
    phone = forms.NumberInput()
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()


# Data by Login account
class Login(forms.Form):
    email = forms.EmailInput()
    password = forms.PasswordInput()