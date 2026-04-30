from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from .forms import Register, Login
from django.contrib import messages


# Register of Client
def register_client(request):
    if request.POST:
        form = Register.objects.create(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            phone = form.cleaned_data["phone"]
            password1 = form.cleaned_data["password1"]
            password2 = form.cleaned_data["password2"]

            if email == '':
                messages.error(request, 'El Email no puede estar vacio')

            elif "@gmail.com" not in email:
                messages.info(request, 'El "@gmail.com" no fue Ingresado en el Email. Intentalo de Nuevo')

            elif password1 != password2:
                messages.info(request, 'Las contraseñas No Coinciden. Ingresa la Contraseña nuevamente')

            else:
                form.save()
                messages.success(request, 'El Registro ha sido Completado')

                context = {
                    "Name": first_name,
                    "Last Name": last_name,
                    "Email": email,
                    "Phone": phone,
                    "Password 1": password1,
                    "Password 2": password2
                }

                return render(request, "", context)

        else:
            messages.info(request, 'El Registro no puede quedar vacio')
            
            return render(request, "")


# Login of Client
def login_client(request):
    if request.method == "POST":
        form = Login()

        if form.is_valid():
            email = form.cleaned_data["email"]
            password1 = form.cleaned_data["password1"]

            client = authenticate(email, password1)

            if "@gmail.com" not in client.email:
                messages.info(request, 'El email no es valido. Ingresalo con el "@gmail.com"')

            else:
                messages.success(request, 'Sesion Iniciada correctamente')

        else:
            form = Login()
            messages.info(request, 'Indica tus datos para Iniciar Sesion')


# Logout of Client
def logout_client(request):
    logout(request)
    messages.info(request, 'Sesion cerrada')
    return redirect('')