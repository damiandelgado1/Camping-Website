from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import Contact, Register, Login


# Contact for Camping
def contact_camping(request):

    if request.POST:
        form = Contact(request.POST)

        if form.is_valid():
            name = form.cleaned_data["name"]
            username = form.cleaned_data["username"]
            phone = form.cleaned_data["phone"]

            form.save()
            return redirect('home')

    else:
        form = Contact()

    return render(request, "home/form.html")


# Register of Client
def register_client(request):

    if request.method == "POST":
        form = Register(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            username = form.cleaned_data["username"]
            phone = form.cleaned_data["phone"]
            password1 = form.cleaned_data["password1"]
            password2 = form.cleaned_data["password2"]

            if username == '':
                messages.add_message(request, messages.ERROR, f'El Email no puede estar vacio')

            elif "@gmail.com" not in username:
                messages.add_message(request, messages.INFO, f'El "@gmail.com" no fue Ingresado en el Email. Intentalo de Nuevo')

            elif password1 != password2:
                messages.add_message(request, messages.INFO, f'Las contraseñas No Coinciden. Ingresa la Contraseña nuevamente')

            else:
                user = User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    password=password1,
                )

                user.save()

                messages.add_message(request, messages.SUCCESS, f'El Registro ha sido Completado')
                return redirect('home')

    else:
        messages.add_message(request, messages.INFO,f'El Registro no puede quedar vacio')
        form = Register()

    return render(request, "home/register.html", {"form": form})


# Login of Client
def login_client(request):

    if request.method == "POST":
        form = Login(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'Sesion Iniciada correctamente')
                return redirect('home')

            else:
                messages.error(request, 'El email no es valido. Ingresalo con el "@gmail.com"')
                print(user)

    else:
        form = Login()
        messages.info(request, 'Indica tus datos para Iniciar Sesion')

    return render(request, "home/login.html", {"form": form})


# Logout of Client
def logout_client(request):
    logout(request)
    messages.info(request, 'Sesion cerrada')
    return redirect('home')