from rest_framework import serializers
from .models import City, PrayerTime


# Сериализатор для модели City
class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


# Сериализатор для модели PrayerTime
class PrayerTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrayerTime
        fields = '__all__'
