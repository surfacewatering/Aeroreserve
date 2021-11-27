
from django.urls import path
from chat import views

app_name = 'chat'

urlpatterns = [
    path('', views.main2, name='main2'),
    path('<str:room_name>/', views.room, name='room')
]