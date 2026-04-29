from django.db import models

# Model with Data by the Cabin
class Cabin(models.Model):
    number = models.IntegerField(verbose_name="Numero de la Cabaña")
    description = models.TextField(verbose_name="Descripcion de la Cabaña")
    rooms = models.IntegerField(verbose_name="Nro. de Habitaciones")
    bathroom = models.IntegerField(verbose_name="Nro. de Baños")
    dining_room = models.CharField(max_length=20, verbose_name="Comedor")
    kitchen = models.CharField(max_length=20, verbose_name="Cocina")
    availability = models.BooleanField(verbose_name="Disponibilidad de la Cabaña")
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"Nueva Cabaña disponible: Nro - {self.number}, Habitaciones - {self.rooms}, Disponibilidad - {self.availability}"

    class Meta:
        verbose_name = "cabin"
        verbose_name_plural = "cabins"