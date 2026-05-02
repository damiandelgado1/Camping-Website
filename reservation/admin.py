from django.contrib import admin
from .models import Reservation

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ["client", "cabin", "persons", "entrance", "exit", "payment"]
    list_filter = ["client", "cabin", "entrance", "exit"]
    search_fields = ["client", "cabin"]