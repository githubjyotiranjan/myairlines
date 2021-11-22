from django.urls import include, path

from rest_framework import routers
from .views import findflightsView, SaveReservationView


urlpatterns = [
   path('', findflightsView.as_view()),
   path('reservation', SaveReservationView.as_view())
]