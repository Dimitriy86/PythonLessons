import json

# --------------------------------------------------------------------------------------------------

some_data = {
    'key': 'value',
    2: [1, 2, 3],
    'my_tuple': (5, 6),
    'my_dict': {'key': 'value'},
}

json_string = json.dumps(some_data)
print(json_string)
unpacked_some_data = json.loads(json_string)
print(unpacked_some_data)

# --------------------------------------------------------------------------------------------------

# Python об'єкт (словник)
data = {"name": "Gupalo Vasyl", "age": 30, "isStudent": True}

# Серіалізація у файл
with open("data.json", 'w', encoding='utf-8') as file:
    json.dump(data, file)

# --------------------------------------------------------------------------------------------------

# Десеріалізація об'єкту
with open('data.json', 'r', encoding='utf-8') as file:
    data_from_file = json.load(file)
    print(data_from_file)

# --------------------------------------------------------------------------------------------------

# Python об'єкт(словник)
data = {"name": "Гупало Василь", "age": 30, "isStudent": True}

# Серіалізація у файл
with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
