import re

# -------------------------------------------------------------------

file_name = "Мій документ Python.txt"
pattern = r"\s"
replacement = "_"
formatted_name = re.sub(pattern, replacement, file_name)

print(formatted_name)

# -------------------------------------------------------------------

text = "Python - потужна, універсальна; мова!"
pattern = r"[;,:!\.]"
replacement = " "
modified_name = re.sub(pattern, replacement, text)

print(modified_name)

# -------------------------------------------------------------------

phone = """
        Михайло Куліш: 050-171-1634,
        Вікторія Кущ: 063-134-1729,
        Оксана Гавриленко: 069-234-5612
        """

pattern = r"(\d{3})-(\d{3})-(\d{2})(\d{2})"
replacement = r"(\1) \2-\3-\4"
formatted_name = re.sub(pattern, replacement, phone)

print(formatted_name)

