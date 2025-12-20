# this_is_string = 'Hi there!'
# the_same_string = 'Hi there!'
# print(this_is_string == the_same_string)

# -------------------------------------------------------------------

# print("spam" "eggs")

# -------------------------------------------------------------------

# s = "Hi there!"

# start = 0
# end = 7

# print(s.find("er", start, end))
# print(s.find("q"))

# -------------------------------------------------------------------

# s = 'Some words'

# print(s.index('o'))
# print(s.rindex('o'))

# -------------------------------------------------------------------

# text = "hello world"
# result = text.split()
# print(result)

# -------------------------------------------------------------------

# text = "apple, banana, cherry"
# result = text.split(',')
# print(result)

# -------------------------------------------------------------------

# list_of_strings = ['hello', 'world']
# result = ' '.join(list_of_strings)
# print(result)

# -------------------------------------------------------------------

# elements = ['earth', 'air', 'fire', 'water']
# result = ', '.join(elements)
# print(result)

# -------------------------------------------------------------------

# clean = '   spacious   '.strip()
# print(clean)

# -------------------------------------------------------------------

# text = "Hello world"
# new_text = text.replace('world', 'Python')
# print(new_text)

# -------------------------------------------------------------------

# text = "one fish, two fish, red fish, blue fish"
# new_text = text.replace('fish', 'bird', 2)
# print(new_text)

# -------------------------------------------------------------------

# text = 'Hello, world!'
# new_text = text.replace('world', '')
# print(new_text)

# -------------------------------------------------------------------

# print('TestHook'.removeprefix('Test'))
# print('TestHook'.removeprefix('Hook'))

# -------------------------------------------------------------------

# print('TestHook'.removesuffix('Test'))
# print('TestHook'.removesuffix('Hook'))

# -------------------------------------------------------------------

# url_search = "<https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t>"
# _, query = url_search.split('?')
# print(query)

# obj_query = {}
# for el in query.split('&'):
#     key, value = el.split('=')
#     obj_query.update({key: value.replace('+', ' ')})
# print(obj_query)

# -------------------------------------------------------------------

# number = '12345'
# print(number.isdigit())

# text = 'Number123'
# print(text.isdigit())

# -------------------------------------------------------------------

# user_input = input("Введіть число: ")
# if user_input.isdigit():
#     print('Це дійсне число')
# else:
#     print("Це не число!")

# -------------------------------------------------------------------

# for char in "Hello 123":
#     if char.isdigit():
#         print(f"{char} - це цифра")
#     else:
#         print(f"{char} - не цифра")

# -------------------------------------------------------------------

# # Метод translate()
# intab = "aeiou"
# outtab = "12345"
# trantab = str.maketrans(intab, outtab)

# str = "This is string example"
# print(str.translate(trantab))

# -------------------------------------------------------------------

# symbols = "0123456789ABCDEF"
# code = [
#         '0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111',
#         '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111'
#         ]

# MAP = {}

# for s, c in zip(symbols, code):
#     MAP[ord(s)] = c
#     MAP[ord(s.lower())] = c

# result = "34 DF 56 AC".translate(MAP)
# print(result)

# -------------------------------------------------------------------

morze_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
              'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
              'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
              'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
              'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
              '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
              '8': '---..', '9': '----.'}

# Перетворення ключів словника на Unicode коди
table_morze_dict = {}
for k, v in morze_dict.items():
    table_morze_dict[ord(k)] = v

string = "Hello world"

result = ""

for ch in string:
    result = result + ch.upper().translate(table_morze_dict)

print(result)

# -------------------------------------------------------------------