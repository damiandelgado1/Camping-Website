from django.shortcuts import render
from django.contrib import messages
from cabin.models import Cabin
from client.forms import Contact


# Main page with Name and Content by WebSite
def main_page(request):
    cabins = Cabin.objects.all()
    return render(request, "home/home.html", {"cabins": cabins})


# About by Camping
def about_site(request):
    return render(request, "home/about.html")



# Contact form
def form_contact(request):
    form = Contact()

    if request.POST:

        if form.is_valid():
            name = form.cleaned_data["Name"]
            email = form.cleaned_data["Email"]
            phone = form.cleaned_data["Phone"]

            form.save()

            messages.success(request, "Gracias por Contactar al Sitio. Te responderemos lo mas Pronto")
            return render(request, "home/form.html")

        else:
            messages.error(request, "Los Datos de Contacto son Incorrectos")

        return render(request, "home/form.html", {"form": form})
    
    return render(request, "home/form.html", {"form": form})