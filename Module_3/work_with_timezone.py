from datetime import datetime, timezone, timedelta

#------------------------------------------------------------

# local_now = datetime.now()
# utc_now = datetime.now(timezone.utc)

# print(local_now)
# print(utc_now)

#------------------------------------------------------------

# utc_time = datetime.now(timezone.utc)

# # Створення часової зони для Східного часового поясу (UTC-5)
# eastern_time = utc_time.astimezone(timezone(timedelta(hours=-5)))
# # Перетворює час UTC в час Східного часового поясу
# print(eastern_time)

#------------------------------------------------------------

# припустимо, місцевий час належить до часової зони UTC+2
# local_timezone = timezone(timedelta(hours=2))
# local_time = datetime(year=2025, month=12, day=13, hour=22, minute=00, second=0, tzinfo=local_timezone)

# # Конвертація локального часу в UTC
# utc_time = local_time.astimezone(timezone.utc)
# print(utc_time)

#------------------------------------------------------------

# Час у конкретній часовій зоні
# timezone_offset = timezone(timedelta(hours=2))
# timezone_datetime = datetime(year=2025, month=12, day=13, hour=22, minute=6, second=30, tzinfo=timezone_offset)

# # Конвертація у формат ISO 8601
# iso_format_with_timezone = timezone_datetime.isoformat()
# print(iso_format_with_timezone)

#------------------------------------------------------------