from collections import namedtuple

# ---------------------------------------------------------------------------------

# # Створення іменованого кортежу
Point = namedtuple('Point', ['x', 'y'])

# # Створення екземпляра Point
p = Point(11, y=11)

# # Доступ до елементів
print(p.x)
print(p.y)

# ---------------------------------------------------------------------------------

# Створення іменованого котрежу Person
Person = namedtuple('Person', ['first_name', 'last_name', 'age', 'birth_place', 'post_index'])

# # Створення екземпляра Person
person = Person('Mick', 'Nitch', 35, 'Boston', '01146')

# # Виведення різних атрибутів шменованого кортежу
print(person.first_name)
print(person.post_index)
print(person.age)
print(person[3])

# ---------------------------------------------------------------------------------

Cat = namedtuple('Cat', ['nickname', 'age', 'owner'])

cat = Cat('Simon', 4, 'Krabat')

print(f"This is a cat {cat.nickname}, {cat.age} age, his owner {cat.owner}")

