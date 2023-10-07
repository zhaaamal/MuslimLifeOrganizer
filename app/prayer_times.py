import praytimes
from datetime import datetime

# Устанавливаем координаты для Бишкека (широта и долгота)
latitude = 42.87  # Широта
longitude = 74.59  # Долгота

# Устанавливаем временную зону для Бишкека
timezone = 6  # Зона времени для Asia/Bishkek (GMT+6)

# Создаем объект PrayTimes и устанавливаем метод расчета (в данном случае, MWL - Muslim World League)
pt = praytimes.PrayTimes()

# Устанавливаем координаты
coordinates = (latitude, longitude)

# Получаем текущую дату и время
now = datetime.now()

# Вычисляем времена намазов
prayer_times = pt.getTimes((now.year, now.month, now.day), coordinates, timezone)

# Список названий намазов
prayer_names = ["Fajr", "Dhuhr", "Asr", "Maghrib", "Isha"]

# Выводим результат
for i in range(5):
    print(f"{prayer_names[i]}: {prayer_times[prayer_names[i].lower()]}")
