from django.contrib import admin

from .models import DiaryEntry, ToDoTask, FastingRecord, Holiday, PrayerTime

admin.site.register(DiaryEntry)
admin.site.register(ToDoTask)
admin.site.register(FastingRecord)
admin.site.register(Holiday)
admin.site.register(PrayerTime)