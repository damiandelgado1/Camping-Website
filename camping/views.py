from django.shortcuts import render
from cabin.models import Cabin


# Main page with Name and Content by WebSite
def main_page(request):
    cabins = Cabin.objects.all()
    return render(request, "home/home.html", {
        "cabins": cabins,
        "es_propietario": request.user.is_staff
    })