from django.urls import path
from .views import PrayerTimeView, DiaryEntryListCreateView, DiaryEntryDetailView,\
    HolidayListCreateView, HolidayDetailView, ToDoTaskListCreateView, ToDoTaskDetailView, FastingRecordListCreateView, \
    FastingRecordDetailView, FastingDebtView

urlpatterns = [
    path('prayer-time/', PrayerTimeView.as_view(), name='prayer-time'),
    path('diary/', DiaryEntryListCreateView.as_view(), name='diary-list-create'),
    path('diary/<int:pk>/', DiaryEntryDetailView.as_view(), name='diary-detail'),
    path('holidays/', HolidayListCreateView.as_view(), name='holiday-list-create'),
    path('holidays/<int:pk>/', HolidayDetailView.as_view(), name='holiday-detail'),
    path('task-list/', ToDoTaskListCreateView.as_view(), name='task-list'),
    path('task-list/<int:pk>/', ToDoTaskDetailView.as_view(), name='task-detail'),
    path('fasting-records/', FastingRecordListCreateView.as_view(), name='fastingrecord-list-create'),
    path('fasting-records/<int:pk>/', FastingRecordDetailView.as_view(), name='fastingrecord-detail'),
    path('fasting-debts/', FastingDebtView.as_view(), name='fastingdebts'),
]

