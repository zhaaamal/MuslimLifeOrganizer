from django.db import models
from django.contrib.auth import get_user_model


MyUser = get_user_model()


# Модель для записей в дневнике
class DiaryEntry(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.PROTECT)  # Связь с пользователем
    date = models.DateField()
    text = models.TextField()


# Модель для задач ToDo
class ToDoTask(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.PROTECT)
    task_text = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    due_date = models.DateField()
    prayer_time = models.TimeField()  # Поле для времени намаза


# Модель для записей о постах
class FastingRecord(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.PROTECT)  # Связь с пользователем
    date = models.DateField()
    missed_days = models.PositiveIntegerField()
    made_up_days = models.PositiveIntegerField()


# Дополнительные модели для календаря праздников и времени намаза
class Holiday(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    description = models.TextField()


class PrayerTime(models.Model):
    date = models.DateField()
    fajr = models.TimeField()
    dhuhr = models.TimeField()
    asr = models.TimeField()
    maghrib = models.TimeField()
    isha = models.TimeField()
