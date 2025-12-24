import re

# -------------------------------------------------------------------

# Знаходження всіх чисел у рядку за допомогою findall

text = "Рік 2025 був, складнішим, ніж 2024"
pattern = r"\d+"
matches = re .findall(pattern, text)

print(matches)

# -------------------------------------------------------------------

text = "Python - це проста, але потужна мова програмування"
pattern = r"\w+"
matches = re.findall(pattern, text)

print(matches)

# -------------------------------------------------------------------

text = "Контакти: example@example.com, example2@sample.org"
pattern = r"\w+@\w+\.\w+"
matches = re.findall(pattern, text)

print(matches)
