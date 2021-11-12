from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from aeroreserve.models import Airlines, Passenger, Ticket, PassengerTicketRel
from django.urls import reverse
from aeroreserve.forms import PassengerForm
from django.forms import formset_factory
import random
import datetime
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
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

@login_required
def index(request):
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

@login_required
def plane_detail_book(request, pk):
    request.session['F_No'] = pk
    if request.method == "POST":
        request.session['N'] = int(request.POST.get("passengers"))
        return HttpResponseRedirect(reverse('passenger_info'))
    else:
        print("ERROR")
    return render(request, 'flightdetail.html', {'flight': pk})

@login_required
def passenger_info(request):
    PassengerFormSet = formset_factory(PassengerForm, extra=request.session.get('N'))
    if request.method == "POST":
        passenger_details = PassengerFormSet(request.POST)
        if passenger_details.is_valid():
            p_ssn = list()
            p_fname = list()
            p_lname = list()
            p_sex = list()
            p_dob = list()
            for K in passenger_details.forms:
                psngr = K.save(commit=False)
                p_ssn.append(psngr.SSN)
                p_fname.append(psngr.passenger_firstname)
                p_lname.append(psngr.passenger_lastname)
                p_dob.append(psngr.passenger_dob.strftime("%m/%d/%Y"))
                p_sex.append(psngr.passenger_gender)
            request.session['p_ssn'] = p_ssn
            request.session['p_fname'] = p_fname
            request.session['p_lname'] = p_lname
            request.session['p_dob'] = p_dob
            request.session['p_sex'] = p_sex
        return HttpResponseRedirect(reverse('payments_page'))
    else:
        passenger_details = PassengerFormSet()
    return render(request,'passenger_info.html', {'passenger_details':passenger_details})

@login_required
def payments_page(request):
    F_No = request.session.get('F_No')
    N = request.session.get('N')
    t = Ticket.objects.all()
    final2 = Airlines.objects.get(airline_id=F_No)
    price = final2.fare
    t_price = price*N
    p_ssn = request.session.get('p_ssn')
    p_fname = request.session.get('p_fname')
    p_lname = request.session.get('p_lname')
    p_dob = request.session.get('p_dob')
    p_sex = request.session.get('p_sex')
    print(request.session.keys())
    if request.method == "POST":
        key = makePNR()
        while t.filter(PNR=key).exists():
            key = makePNR()
        T = Ticket(PNR=key, username=request.user, Date_of_booking=datetime.date.today(), fk_flights=final2)
        T.save()
        for k in range(0, N):
            p = Passenger(SSN=p_ssn[k], passenger_firstname=p_fname[k], passenger_lastname=p_lname[k],
            passenger_gender=p_sex[k].lower(), passenger_dob=datetime.datetime.strptime(p_dob[k], "%m/%d/%Y"))
            p.save()
            p_rel = PassengerTicketRel(PNR=T, SSN=p)
            p_rel.save()
        request.session['key'] = key
        return HttpResponseRedirect(reverse('congrats'))
    return render(request, 'payments_page.html', {'price': t_price})

@login_required
def congrats(request):
    t = Ticket.objects.get(PNR=request.session['key'])
    return render(request, 'congrats.html', {'ticket': t})

@login_required
def bookedtickets(request, pk):
    tickets = Ticket.objects.filter(username=request.user).select_related('fk_flights')
    p = tickets.filter(PNR=pk).prefetch_related('PNR__passengerticketrel_set__SSN')
    t_price = p[0].passengerticketrel_set.count() * p[0].fk_flights.fare
    psngr = p[0].passengerticketrel_set.all()
    context = {
        'passenger': psngr,
        'ticket': p[0],
        't_price': t_price
    }
    return render(request, 'bookedtickets.html', context)

@login_required
def ticketlist(request):
    tickets = Ticket.objects.filter(username=request.user).select_related('fk_flights')
    context = {
        'tickets': tickets
    }
    return render(request, 'ticketlist.html', context)

def makePNR():
    PNR = ''
    while len(PNR) < 8:
        n = random.randint(0, 9)
        PNR = PNR + str(n)
    k = int(PNR)
    return k