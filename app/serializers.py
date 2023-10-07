from rest_framework import serializers
from .models import PrayerTime  # Замените '.models' на путь к вашей модели


class PrayerTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrayerTime
        fields = '__all__'  # Включить все поля модели PrayerTime
