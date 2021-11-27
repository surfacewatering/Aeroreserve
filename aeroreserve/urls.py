from django.contrib import admin
from django.urls import path
from aeroreserve import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("", views.main, name="main"),
    path("login/", LoginView.as_view(), name="login"),
    path("register/", views.register, name="register"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("index", views.index, name="index"),
    path("index/<slug:pk>/", views.plane_detail_book, name="plane_detail_book"),
    path("payment", views.payments_page, name="payments_page"),
    path("congrats", views.congrats, name="congrats"),
    path("tickets/<int:pk>/", views.bookedtickets, name="bookedtickets"),
    path("ticketlist", views.ticketlist, name="ticketlist"),
    path("passenger_info", views.passenger_info, name="passenger_info")
]