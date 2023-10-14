from rest_framework import generics, views, status
from rest_framework.response import Response
from datetime import datetime
import praytimes
from .models import PrayerTime, DiaryEntry, Holiday, ToDoTask, FastingRecord, MyUser
from .permissions import IsAdminOrReadOnly
from .serializers import PrayerTimeSerializer, DiaryEntrySerializer, HolidaySerializer, ToDoTaskSerializer, \
    FastingRecordSerializer


class PrayerTimeView(generics.RetrieveAPIView):
    serializer_class = PrayerTimeSerializer

    def get(self, request, *args, **kwargs):
        latitude = 42.87  # Широта
        longitude = 74.59  # Долгота
        timezone = 6  # Зона времени для Asia/Bishkek (GMT+6)

        # Создаем объект PrayTimes и устанавливаем метод расчета (в данном случае, MWL - Muslim World League)
        pt = praytimes.PrayTimes()
        coordinates = (latitude, longitude)

        # Получаем текущую дату и время
        now = datetime.now()

        # Вычисляем времена намазов
        prayer_times = pt.getTimes((now.year, now.month, now.day), coordinates, timezone)

        # Создаем объект PrayerTime, заполняем его данными и сохраняем в базе данных
        prayer_time, is_created = PrayerTime.objects.get_or_create(
            date=now.date(),
            fajr=prayer_times["fajr"],
            dhuhr=prayer_times["dhuhr"],
            asr=prayer_times["asr"],
            maghrib=prayer_times["maghrib"],
            isha=prayer_times["isha"]
        )

        # Сериализуем объект PrayerTime и возвращаем его
        serializer = self.get_serializer(prayer_time)
        return Response(serializer.data)


class DiaryEntryListCreateView(generics.ListCreateAPIView):
    queryset = DiaryEntry.objects.all()
    serializer_class = DiaryEntrySerializer


class DiaryEntryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DiaryEntry.objects.all()
    serializer_class = DiaryEntrySerializer


class HolidayListCreateView(generics.ListCreateAPIView):
    queryset = Holiday.objects.all()
    serializer_class = HolidaySerializer
    permission_classes = [IsAdminOrReadOnly]  # Применить пользовательское право доступа


class HolidayDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Holiday.objects.all()
    serializer_class = HolidaySerializer
    permission_classes = [IsAdminOrReadOnly]  # Применить пользовательское право доступа


class ToDoTaskListCreateView(generics.ListCreateAPIView):
    queryset = ToDoTask.objects.all()
    serializer_class = ToDoTaskSerializer


class ToDoTaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToDoTask.objects.all()
    serializer_class = ToDoTaskSerializer


class FastingRecordListCreateView(generics.ListCreateAPIView):
    queryset = FastingRecord.objects.all()
    serializer_class = FastingRecordSerializer


class FastingRecordDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FastingRecord.objects.all()
    serializer_class = FastingRecordSerializer


class FastingDebtsView(views.APIView):
    def get(self, request, format=None):
        user = request.user.id
        fasting_records = FastingRecord.objects.filter(user=user)

        total_debts = 0
        debts_in_dates = {}

        for record in fasting_records:
            if not record.fasted:
                total_debts += 1
                debts_in_dates[record.date] = True

        response_data = {
            'total_debts': total_debts,
            'debts_in_dates': debts_in_dates
        }

        return Response(response_data, status=status.HTTP_200_OK)
