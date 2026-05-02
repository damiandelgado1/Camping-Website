from django import forms


# Contact form for Contact to Site
class Contact(forms.Form):
    name = forms.CharField(max_length=20)
    username = forms.EmailField()
    phone = forms.IntegerField()


# Data by Resgiter account
class Register(forms.Form):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    username = forms.EmailField()
    phone = forms.IntegerField()
    password1 = forms.CharField(max_length=20, widget=forms.PasswordInput())
    password2 = forms.CharField(max_length=20, widget=forms.PasswordInput())


# Data by Login account
class Login(forms.Form):
    username = forms.EmailField()
    password = forms.CharField(max_length=20, widget=forms.PasswordInput())