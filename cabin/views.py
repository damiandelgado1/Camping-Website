from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from cabin.models import Cabin


# Display all Cabin's
class ShowCabin(ListView):
    model = Cabin
    template_name = "cabin/list_cabin.html"
    context_object_name = "cabins"


# Display details by the Cabin's
class DetailCabin(DetailView):
    model = Cabin
    template_name = "cabin/detail_cabin.html"
    context_object_name = "cabin"


# Manage all Cabin in the Camping
class ManageCabin(ListView):
    model = Cabin
    template_name = "dashboard/manage_cabin.html"
    context_object_name = "cabins"


# See detail of the a Cabin in the camping
class EditCabin(DetailView):
    model = Cabin
    template_name = "dashboard/edit_cabin.html"
    context_object_name = "cabin"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["es_propietario"] = self.request.user.is_staff
        return context


# Create a Cabin for reserve
class CreateCabin(UserPassesTestMixin, CreateView):
    model = Cabin
    fields = [
        "number",
        "preview",
        "description",
        "rooms",
        "bathroom",
        "dining_room",
        "kitchen",
        "availability",
        "price"
    ]
    template_name = "dashboard/create_cabin.html"
    success_url = reverse_lazy("home")

    def test_func(self):
        return self.request.user.is_staff


# Delete a Cabin for reserve
class DeleteCabin(UserPassesTestMixin, DeleteView):
    model = Cabin
    template_name = "dashboard/delete_cabin.html"
    success_url = reverse_lazy("home")

    def test_func(self):
        return self.request.user.is_staff