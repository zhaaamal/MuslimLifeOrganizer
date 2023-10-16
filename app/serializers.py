from rest_framework import serializers
from .models import PrayerTime, DiaryEntry, MyUser, Holiday, ToDoTask, FastingRecord


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


class ToDoTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoTask
        fields = '__all__'


class FastingRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = FastingRecord
        fields = '__all__'


class FastingDebtSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username')
    fasted = serializers.BooleanField()

    class Meta:
        model = FastingRecord
        fields = ['user', 'date', 'fasted']
