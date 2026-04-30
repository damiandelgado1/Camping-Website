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
            cabin = form.cleaned_data["cabin"]
            persons = form.cleaned_data["persons"]
            entrance = form.cleaned_data["entrance"]
            exit = form.cleaned_data["exit"]
            payment = form.cleaned_data["payment"]

            stay = Cabin()

            if exit == '':
                messages.info(request, "No puedes dejar la Fecha de Salida sin confirmar")

            elif exit > entrance:
                messages.info("La Fecha de Salida no puede ser antes que la de Entrada")

            elif persons > stay.rooms:
                messages.info(request, "El Nro. de Personas supera la cantidad de Habitaciones de la Cabaña")

            elif payment < stay.price:
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


# Cancel a Reservation
@login_required
def cancel_reservation(request):
    if request.POST:
        form = Reservation()
        form.delete()

        messages.info(request, "Reserva cancelada")
        return render(request, "")