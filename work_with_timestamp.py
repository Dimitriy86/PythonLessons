from datetime import datetime

#------------------------------------------------------------

# Конвертація datetime в timestamp

# Поточний час
# now = datetime.now()

# Конвертація datetime в timestamp
# timestamp = datetime.timestamp(now)
# print(timestamp)

#------------------------------------------------------------

# Конвертація timedtamp в datetime

# Припустимо, є timestamp
timestamp = 1617183600

# Конвертація timestamp нназад у datetime
dt_object = datetime.fromtimestamp(timestamp=timestamp)
print(dt_object)

#------------------------------------------------------------
