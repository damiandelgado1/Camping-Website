from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakeReservation
from .models import Reservation
from cabin.models import Cabin


# Create a Reservation
@login_required
def create_reservation(request):
    if request.method == "POST":
        form = MakeReservation(request.POST)

        if form.is_valid():
            client = form.cleaned_data["client"]
            cabin = form.cleaned_data["cabin"]
            persons = form.cleaned_data["persons"]
            entrance = form.cleaned_data["entrance"]
            exit = form.cleaned_data["exit"]
            payment = form.cleaned_data["payment"]

            stay = cabin

            if exit == '':
                messages.info(request, "No puedes dejar la Fecha de Salida sin confirmar")
                return render(request, "reservation/create_reservation.html", {"form": form})


            elif exit < entrance:
                messages.info(request, "La Fecha de Salida no puede ser antes que la de Entrada")
                return render(request, "reservation/create_reservation.html", {"form": form})


            elif persons > stay.rooms:
                messages.info(request, "El Nro. de Personas supera la cantidad de Habitaciones de la Cabaña")
                return render(request, "reservation/create_reservation.html", {"form": form})


            elif payment < stay.price:
                messages.info(request, "La cantidad de Dinero para pagar la Reserva es Insuficiente")
                return render(request, "reservation/create_reservation.html", {"form": form})


            else:
                form.save()
                messages.success(request, "La Reserva se creo correctamente")
                return redirect("home")

        else:
            messages.info(request, "La Reserva no puede quedar con Datos sin Ingresar")
            return render(request, "reservation/create_reservation.html")

    else:
        form = MakeReservation()
        return render(request, "reservation/create_reservation.html", {"form": form})


# Cancel a Reservation
@login_required
def cancel_reservation(request):
    if request.method == "POST":
        form = Reservation()
        form.delete()

        messages.info(request, "Reserva cancelada")
        return redirect("home")
    
    else:
        return render("home/home.html")