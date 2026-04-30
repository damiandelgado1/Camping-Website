from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakeReservation
from .models import Reservation
from cabin.models import Cabin


# Create a Reservation
@login_required
def create_reservation(request):
    if request.POST:
        form = MakeReservation(request.POST)

        if form.is_valid():
            client = form.cleaned_data["client"]
            persons = form.cleaned_data["persons"]
            entrance = form.cleaned_data["entrance"]
            exit = form.cleaned_data["exit"]
            payment = form.cleaned_data["payment"]

            cabin = Cabin()

            if exit == '':
                messages.info(request, "No puedes dejar la Fecha de Salida sin confirmar")

            elif exit > entrance:
                messages.info("La Fecha de Salida no puede ser antes que la de Entrada")

            elif persons > cabin.rooms:
                messages.info(request, "El Nro. de Personas supera la cantidad de Habitaciones de la Cabaña")

            elif payment < cabin.price:
                messages.info(request, "La cantidad de Dinero para pagar la Reserva es Insuficiente")

            else:
                context = {
                    "Cliente": client,
                    "Cabaña": cabin,
                    "Personas": persons,
                    "Entrada": entrance,
                    "Salida": exit,
                    "Pago": payment,
                }

                form.save()
                messages.success(request, "La Reserva se creo correctamente", context)
                return render(request, "")

        else:
            messages.info(request, "La Reserva no puede quedar con Datos sin Ingresar")
            return render(request, "")


# Modify a Reservation
@login_required
def modify_reservation(request, name):
    if request.POST:
        form = Reservation.objects.get(client=name)
        cabin = Cabin()

        if form.is_valid():
            persons = form.cleaned_data["persons"]
            entrance = form.cleaned_data["entrance"]
            exit = form.cleaned_data["exit"]

            if entrance != True:
                messages.info(request, "La nueva Fecha de Entrada No esta Disponible")

            elif persons > cabin.rooms:
                messages.info(request, "El nro. de Personas supera el maximo permitido en la Cabaña")

            else:
                context = {
                    "Personas": persons,
                    "Entrada": entrance,
                    "Salida": exit,
                }

                form.save()
                messages.success(request, "Reserva modificada Correctamente", context)
                return render(request, )


# Cancel a Reservation
@login_required
def cancel_reservation(request):
    if request.POST:
        form = Reservation()
        form.delete()

        messages.info(request, "Reserva cancelada")
        return render(request, )