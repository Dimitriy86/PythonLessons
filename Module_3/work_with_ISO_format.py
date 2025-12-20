from datetime import datetime

#------------------------------------------------------------

# Поточна дата і час
# now = datetime.now()

# # Конвертація у формат ISO 8601
# iso_format = now.isoformat()
# print(iso_format)

#------------------------------------------------------------

# iso_date_string = "2025-12-13T21:37:30.356985"

# # Конвертація з ISO формату
# date_from_iso = datetime.fromisoformat(iso_date_string)
# print(date_from_iso)

#------------------------------------------------------------

# Метод isoweekday()

# Створення об'єкта datetime
# now = datetime.now()

# # Використання isoweekday() для отримання дня тижня
# day_of_week = now.isoweekday()

# print(f"Сьогодні: {day_of_week}")

#------------------------------------------------------------

# Метод isocalendar()

# Створення об'єкта datetime
now = datetime.now()

# Отримання ISO календаря
iso_calendar = now.isocalendar()

print(f"ISO рік: {iso_calendar[0]}, ISO тиждень: {iso_calendar[1]}, ISO день тижня: {iso_calendar[2]}")
