import random

# ---------------------------------------------------------------

# Метод randint()
# dice_roll = random.randint(1, 6)
# print(f"Ви кинули {dice_roll}")

# ---------------------------------------------------------------

# Метод random()
# num = random.random()
# print(num)

# ---------------------------------------------------------------

# fill_percentage = random.random() * 100
# print(f"Заповнення: {fill_percentage:.2f}%")

# ---------------------------------------------------------------

# Метод randrange(start, stop[, step])

# print(random.randrange(1, 11, 2))

# ---------------------------------------------------------------

# # Метод shuffle(x)
# cards = ["Туз", "Король", "Дама", "Валет", "10", "9", "8", "7", "6"]

# random.shuffle(cards)
# print(f"Перемішана колода: {cards}")

# ---------------------------------------------------------------

# Метод chiose(seq) - один елемент
# fruits = ['apple', 'banana', 'orange']
# print(random.choice(fruits))

# ---------------------------------------------------------------

# Метод choises() - вибрати два і більше елементів з колекції
# items = ['apple', 'banana', 'cherry', 'melon']
# chosen_item = random.choices(items, k=1)
# print(chosen_item)

# ---------------------------------------------------------------

# Вибрати кілька елементів
# numbers = [1, 2, 3, 4, 5]
# chosen_numbers = random.choices(numbers, k=3)
# print(chosen_numbers)

# ---------------------------------------------------------------

# Вибір з вагами
# colors = ['red', 'green', 'blue']
# wieghts = [10, 1, 1]
# chosen_color = random.choices(colors, wieghts, k=1)
# print(chosen_color)

# ---------------------------------------------------------------

# Метод sample()
# participants = ['Anna', 'Bogdan', 'Viktor', 'Haluna', 'Dmytro', 'Olena', 'Evgen', 'Zorian', 'Ihor', 'Josyp']
# team = random.sample(participants, 4)
# print(f"Team is: {team}")

# ---------------------------------------------------------------

# uniform()
price = random.uniform(50, 100)
print(f"Випадкова ціна: {price:.2f}")

# ---------------------------------------------------------------