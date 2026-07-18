from django.urls import path
from django.contrib import admin
from .views import ReservationList, ReservationDetail, create_reservation, cancel_reservation


app_name = "reservation"

urlpatterns = [
    path('list/', ReservationList.as_view(), name="list_reservation"),
    path('detail/<int:pk>/', ReservationDetail.as_view(), name="detail_reservation"),
    path('create/', create_reservation, name="create_reservation"),
    path('cancel/<int:pk>/', cancel_reservation, name="cancel_reservation"),
    path('admin/', admin.site.urls),
]