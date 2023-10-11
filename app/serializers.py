from rest_framework import serializers
from .models import PrayerTime, DiaryEntry, MyUser, Holiday


class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('username', 'email')


class PrayerTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrayerTime
        fields = '__all__'


class DiaryEntrySerializer(serializers.ModelSerializer):
    user = MyUserSerializer()

    class Meta:
        model = DiaryEntry
        fields = '__all__'


class HolidaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Holiday
        fields = '__all__'

