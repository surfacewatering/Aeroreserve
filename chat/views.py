from django.shortcuts import render

# Create your views here.

def main2(request):
    return render(request, 'main2.html')

def room(request, room_name):
    username = request.GET.get('username', 'Anonymous')
    return render(request, 'room.html', {'room_name': room_name, 'username': username})
