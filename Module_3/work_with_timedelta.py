from datetime import datetime, timedelta

# delta = timedelta(
#     days=50,
#     seconds=27,
#     microseconds=10,
#     milliseconds=29000,
#     minutes=5,
#     hours=8,
#     weeks=2
# )
# print(delta)

#------------------------------------------------------------

# seventh_day_2019 = datetime(year=2019, month=1, day=7, hour=14)
# seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)

# difference = seventh_day_2020 - seventh_day_2019
# print(difference)
# print(difference.total_seconds())

#------------------------------------------------------------

# now = datetime.now()
# future_time = now + timedelta(days=10)
# print(future_time)

#------------------------------------------------------------

# Від якоїсь конкретної дати
# sixth_day_2025 = datetime(year=2025, month=12, day=13, hour=20)
# four_week_interval = timedelta(weeks=4)

# print(sixth_day_2025 + four_week_interval)
# print(sixth_day_2025 - four_week_interval)

#------------------------------------------------------------

# Створення об'єкта datetime
# date = datetime(year=2025, month=12, day=13)

# # Отримання порядкового номера
# ordinal_number = date.toordinal()
# print(f"Порядковий номер дати {date} становить {ordinal_number}")

#------------------------------------------------------------

# Скільки повних днів пройшло, коли Наполеон спалив Москву

# Встановлення дати спалення Москви Наполеоном (14 вересня 1812 року)
napoleon_burns_moskow = datetime(year=1812, month=9, day=14)

# Поточна дата
# current_time = datetime.now()

# Розрахунок кількості днів
# day_since = current_time.toordinal() - napoleon_burns_moskow.toordinal()
# print(day_since)

#------------------------------------------------------------

