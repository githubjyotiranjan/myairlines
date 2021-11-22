from rest_framework import serializers
from .models import Flights

# class FlightSerializer(serializers.ModelSerializer):
#     flight_number = serializers.CharField(max_length=200)
#     # departure_city = serializers.CharField(max_length=200)
#     # arrival_city = serializers.CharField(max_length=200)
#     # date_of_departure = serializers.DateField(blank=True, null=True)
#     # departure_time = serializers.TimeField(blank=True, null=True)
#
#     class Meta:
#         model = Flights
#         fields = ('__all__')

# todo/api/serializers.py
from rest_framework import serializers
from .models import Flights, Passenger, Reservation

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flights
        fields = ["flight_number", "departure_city", "arrival_city", "date_of_departure", "departure_time"]





class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['flight',
                  'passanger'
                  ]