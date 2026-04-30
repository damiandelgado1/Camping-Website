from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from .forms import Contact, Register, Login
from django.contrib import messages


# Contact for Camping
def contact_camping(request):
    if request.POST:
        form = Contact()

        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            phone = form.cleaned_data["phone"]

            form.save()
            return render(request, "home/form.html")


# Register of Client
def register_client(request):
    if request.method == "GET":
        form = Register()

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

                return render(request, "home/register.html")

        else:
            messages.info(request, 'El Registro no puede quedar vacio')
            return render(request, "home/register.html")
    
    return render(request, "home/register.html")


# Login of Client
def login_client(request):
    if request.GET:
        form = Login()

        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            client = authenticate(email, password)

            if "@gmail.com" not in client.email:
                messages.info(request, 'El email no es valido. Ingresalo con el "@gmail.com"')

            else:
                messages.success(request, 'Sesion Iniciada correctamente')

                return render(request, "home/login.html")

        else:
            form = Login()
            messages.info(request, 'Indica tus datos para Iniciar Sesion')


# Logout of Client
def logout_client(request):
    logout(request)
    messages.info(request, 'Sesion cerrada')
    return redirect('home')