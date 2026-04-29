from django import forms

class Register(forms.Form):
    first_name = forms.TextInput(require=True, verbose_name="Nombre")
    last_name = forms.TextInput(require=True, verbose_name="Apellido")
    email = forms.EmailField(require=True, verbose_name="Email")
    phone = forms.NumberInput(require=True, verbose_name="Telefono")
    password1 = forms.PasswordInput(require=True)
    password2 = forms.PasswordInput(require=True)


class Login(forms.Form):
    email = forms.EmailInput(require=True)
    password1 = forms.PasswordInput(require=True)