from django.db import models


# Create your models here.


class Flights(models.Model):
    flight_number = models.CharField(max_length=200)
    departure_city = models.CharField(max_length=200)
    arrival_city = models.CharField(max_length=200)
    date_of_departure = models.DateField(blank=True, null=True)
    departure_time = models.TimeField(blank=True, null=True)

class Passenger(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone_number = models.IntegerField()

class Reservation(models.Model):
      flight = models.ForeignKey(Flights, on_delete=models.CASCADE)
      passenger = models.OneToOneField(Passenger, on_delete=models.CASCADE)
