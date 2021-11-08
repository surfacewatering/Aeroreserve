# Register your models here.
from django.contrib import admin
from aeroreserve.models import Airlines, Passenger, FlightCosts, PassengerDetails, BookingDetails, Ticket, PassengerTicketRel
from aeroreserve.models import Destination

admin.site.register(Airlines)
admin.site.register(PassengerDetails)
admin.site.register(BookingDetails)
admin.site.register(Destination)
admin.site.register(FlightCosts)
admin.site.register(Passenger)
admin.site.register(Ticket)
admin.site.register(PassengerTicketRel)
