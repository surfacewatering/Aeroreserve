from django.contrib import admin
from django.urls import path
from aeroreserve import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("", views.main, name='main'),
    path("login", LoginView.as_view(), name="login"),
    path("register", views.register, name="register"),
    path("logout", LogoutView.as_view(next_page="main"), name="logout"),
    path("about", views.about, name='about'),
    path("contact", views.contact, name='contact'),
    path("index", views.index, name='index'),
]