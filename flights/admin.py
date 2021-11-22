from django.contrib import admin

from .models import Flights, Reservation, Passenger
# Register your models to admin site, then you can add, edit, delete and search your models in Django admin site.
admin.site.register(Flights)
admin.site.register(Passenger)
admin.site.register(Reservation)
# Register your models here.
