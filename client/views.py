from django.shortcuts import render, redirect
from django.contrib.auth import authenticate ,login, logout
from .forms import Contact, Register, Login
from django.contrib import messages
from .models import Client


# Contact for Camping
def contact_camping(request):

    if request.POST:
        form = Contact(request.POST)

        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            phone = form.cleaned_data["phone"]

            form.save()
            return redirect('home')


# Register of Client
def register_client(request):

    if request.method == "POST":
        form = Register(request.POST)

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
                register = Client.objects.create(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    phone=phone,
                    password1=password1,
                    password2=password2,
                )

                register.save()

                messages.success(request, 'El Registro ha sido Completado')
                return redirect('home')

    else:
        messages.info(request, 'El Registro no puede quedar vacio')
        form = Register()

    return render(request, "home/register.html", {"form": form})


# Login of Client
def login_client(request):

    if request.method == "POST":
        form = Login(request.POST)

        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            client = Client.objects.filter(email=email, password1=password).first()

            if client:
                request.session['client_id'] = client.id
                messages.success(request, 'Sesion Iniciada correctamente')
                return redirect('home')

            else:
                messages.error(request, 'El email no es valido. Ingresalo con el "@gmail.com"')
                print(client)

    else:
        form = Login()
        messages.info(request, 'Indica tus datos para Iniciar Sesion')

    return render(request, "home/login.html", {"form": form})


# Logout of Client
def logout_client(request):
    logout(request)
    messages.info(request, 'Sesion cerrada')
    return redirect('home')