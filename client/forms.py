from django import forms


# Contact form for Contact to Site
class Contact(forms.Form):
    name = forms.CharField(max_length=20)
    email = forms.EmailField()
    phone = forms.IntegerField()


# Data by Resgiter account
class Register(forms.Form):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField()
    phone = forms.IntegerField()
    password1 = forms.CharField(max_length=20)
    password2 = forms.CharField(max_length=20)


# Data by Login account
class Login(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=20)