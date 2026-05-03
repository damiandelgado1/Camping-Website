from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from cabin.models import Cabin


# Display all Cabin's
class ListCabin(ListView):
    model = Cabin
    template_name = "cabin/list_cabin.html"
    context_object_name = "cabins"


# Display details by the Cabin's
class DetailCabin(DetailView):
    model = Cabin
    template_name = "cabin/detail_cabin.html"
    context_object_name = "cabin"


# Create a Cabin for reserve
class CreateCabin(CreateView):
    model = Cabin
    fields = [
        "number",
        "description",
        "rooms",
        "bathroom",
        "dining_room",
        "kitchen",
        "availability",
        "price"
    ]
    template_name = "cabin/create_cabin.html"
    success_url = reverse_lazy("home")


# Delete a Cabin for reserve
class DeleteCabin(DeleteView):
    model = Cabin
    template_name = "cabin/create_cabin.html"
    success_url = reverse_lazy("home")