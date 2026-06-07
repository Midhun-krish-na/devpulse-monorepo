from django.urls import path
from .views import DailyPulseListCreateAPIView


urlpatterns =[
    path('pulse/', DailyPulseListCreateAPIView.as_view(), name='pulse-list-create'),
]
