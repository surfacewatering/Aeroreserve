from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from aeroreserve.models import Airlines, Airport, PaymentInfo, PassengerDetails, BookingDetails, Destination,FlightCosts

# Create your views here.

def main(request):
    return render(request, 'main.html')

def login(request):
    return render(request, 'registration/login.html')

def logout(request):
    return render(request, 'main.html')

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login.html')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form':form})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

@login_required()
def index(request):
    flights = Airlines.objects.all()
    cities = Airlines.objects.values_list('from_field', flat=True)
    cities2 = Airlines.objects.values_list('to', flat=True)
    if request.method == "POST":
        l1 = request.POST.get("from_field")
        l2 = request.POST.get("to")
        flights = Airlines.objects.filter(from_field=l1, to=l2)
    else:
        flights = Airlines.objects.all()
    context = {
        'cities': cities,
        'cities2': cities2,
        'flights': flights,
    }
    return render(request, 'index.html', context)