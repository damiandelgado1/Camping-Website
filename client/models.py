from django.db import models

# Model with Data of the Client
class Client(models.Model):
    first_name = models.CharField(max_length=20, verbose_name="Nombre del Cliente")
    last_name = models.CharField(max_length=20, verbose_name="Apellido del Cliente")
    email = models.EmailField(max_length=20, verbose_name="Email")
    phone = models.IntegerField(verbose_name="Nro. Telefono")
    password1 = models.CharField(max_length=15)
    password2 = models.CharField(max_length=15)

    def __str__(self):
        return f"Cliente {self.first_name} {self.last_name}"