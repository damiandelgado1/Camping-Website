from django.contrib import admin
from .models import Cabin

@admin.register(Cabin)
class CabinAdmin(admin.ModelAdmin):
    list_display = ["number", "description", "rooms", "bathroom", "dining_room", "kitchen", "availability", "price"]
    list_filter = ["number", "availability", "price"]
    search_fields = ["number", "rooms", "price"]