# Register your models here.
from django.contrib import admin
from aeroreserve.models import Airlines, FlightCosts, PaymentInfo, PassengerDetails, Airport, BookingDetails
from aeroreserve.models import Destination

admin.site.register(Airlines)
admin.site.register(PassengerDetails)
admin.site.register(BookingDetails)
admin.site.register(Airport)
admin.site.register(Destination)
admin.site.register(FlightCosts)
admin.site.register(PaymentInfo)
