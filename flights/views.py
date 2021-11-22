from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Flights, Passenger, Reservation
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from .serializers import FlightSerializer, ReservationSerializer


class findflightsView(APIView):
    def post(self, request, *args, **kwargs):
        arrival_city = request.data.get('arrival_city')
        departing_city = request.data.get('departing_city')
        date_of_departure = request.data.get('date_of_departure')
        # departing_city, arrival_city and date_of_departure is mandatory parameter to search a flight
        if departing_city is not None and arrival_city is not None and date_of_departure is not None:
            data = Flights.objects.filter(departure_city=departing_city, arrival_city=arrival_city,
                                          date_of_departure=date_of_departure)
        serializer = FlightSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SaveReservationView(APIView):
    def post(self, request, *args, **kwargs):
        data = {
            "flight": request.data.get('flight'),
            "passanger": request.data.get('passanger')
        }
        data = JSONParser().parse(request)
        reservation_serializer = ReservationSerializer(data=data)
        # Reservation.objects.create(flight = 2
        #                            , passanger = 2)
        return Response("Resevation Created", status=status.HTTP_201_OK)

