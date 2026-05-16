from django.urls import path
from django.contrib import admin
from .views import ShowCabin, DetailCabin, ManageCabin, EditCabin, CreateCabin, DeleteCabin

app_name = "cabin"

urlpatterns = [
    path('list/', ShowCabin.as_view(), name="cabin_list"),
    path('detail/<int:pk>/', DetailCabin.as_view(), name="cabin_detail"),
    path('manage/', ManageCabin.as_view(), name="cabin_manage"),
    path('edit/<int:pk>/', EditCabin.as_view(), name="cabin_edit"),
    path('create/', CreateCabin.as_view(), name="create_cabin"),
    path('delete/<int:pk>/', DeleteCabin.as_view(), name="delete_cabin"),
    path('admin/', admin.site.urls),
]