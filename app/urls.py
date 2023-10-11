from django.urls import path
from .views import PrayerTimeView, DiaryEntryListCreateView, DiaryEntryDetailView,\
    HolidayListCreateView, HolidayDetailView

urlpatterns = [
    path('prayer-time/', PrayerTimeView.as_view(), name='prayer-time'),
    path('diary/', DiaryEntryListCreateView.as_view(), name='diary-list-create'),
    path('diary/<int:pk>/', DiaryEntryDetailView.as_view(), name='diary-detail'),
    path('holidays/', HolidayListCreateView.as_view(), name='holiday-list-create'),
    path('holidays/<int:pk>/', HolidayDetailView.as_view(), name='holiday-detail'),
]

