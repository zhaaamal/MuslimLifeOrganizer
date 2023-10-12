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
    title = models.CharField(max_length=125)
    user = models.ForeignKey(MyUser, on_delete=models.PROTECT)
    task_text = models.CharField(max_length=255)
    is_done = models.BooleanField(default=False)
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Модель для записей о постах
class FastingRecord(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.PROTECT)  # Связь с пользователем
    date = models.DateField()
    fasted = models.BooleanField(default=True)


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
