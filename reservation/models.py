from django.db import models
from django.contrib.auth.models import User
from cabin.models import Cabin

# Information about Reservation by Client
class Reservation(models.Model):
    client = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name="Cliente que hace la Reserva")
    cabin = models.ForeignKey(Cabin, on_delete = models.CASCADE, verbose_name="Cabaña reservada por el Cliente")
    persons = models.IntegerField(verbose_name="Nro. de Personas en la Reserva")
    entrance = models.DateField(verbose_name="Fecha de Entrada")
    exit = models.DateField(verbose_name="Fecha de Salida")
    payment = models.DecimalField(max_digits=6, decimal_places=3)

    def __str__(self):
        return f"Cabaña {self.cabin} reservada por {self.client}"