from django.shortcuts import render

# About by Camping
def about_site(request):
    return render(request, "home/about.html")