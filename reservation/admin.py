from django.contrib import admin
from .models import Reservation

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ["client", "cabin"]
    list_filter = ["cabin"]
    search_fields = ["client", "cabin"]