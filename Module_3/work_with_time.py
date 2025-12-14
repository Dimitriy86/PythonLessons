import time

# ---------------------------------------------------------------

# # Метод time.time()
# current_time = time.time()
# print(f"Поточний час:{current_time}")

# ---------------------------------------------------------------

# Метод time.sleep(seconds)
# print("Початок паузи")
# time.sleep(5)
# print("Кінець паузи")

# ---------------------------------------------------------------

# Метод time.ctime([seconds])
# current_time = time.time()
# print(f"Поточний час: {current_time}")

# readable_time = time.ctime(current_time)
# print(f"Читабельний час: {readable_time}")

# ---------------------------------------------------------------

# Метод time.localtime([seconds])
# current_time = time.time()
# print(f"Поточний час: {current_time}")

# local_time = time.localtime(current_time)
# print(f"Мічцевий час: {local_time}")

# ---------------------------------------------------------------

# Метод time.perf_counter()

# Записуємо час на початку виконання
# start_time = time.perf_counter()

# # Виконуємо якусь операцію
# for _ in range(1_000_000_000):
#     pass # Просто проходить цикл мільон разів

# # Записуємо час після виконання операції
# end_time = time.perf_counter()

# # Розраховуємо та виводимо час виконання
# execution_time = end_time - start_time
# print(execution_time)

# ---------------------------------------------------------------

