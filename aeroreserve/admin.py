# Register your models here.
from django.contrib import admin
from aeroreserve.models import Airlines, Passenger, Ticket, PassengerTicketRel

admin.site.register(Airlines)
admin.site.register(Passenger)
admin.site.register(Ticket)
admin.site.register(PassengerTicketRel)
