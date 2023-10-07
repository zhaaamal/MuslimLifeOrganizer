from django.urls import path
from .views import PrayerTimeView

urlpatterns = [
    path('prayer-time/', PrayerTimeView.as_view(), name='prayer-time'),
]
