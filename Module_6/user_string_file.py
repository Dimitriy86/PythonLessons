from collections import UserString

# ------------------------------------------------------------------------------------

# Створення класу, який розширює UserString
class MyString(UserString):
    # Додавання методу, який перевіряє, чи рядок є палідромом
    def is_palidrome(self):
        return self.data == self.data[::-1]

# Створення екземпляру MyString
my_string = MyString('radar')
print("Row: ", my_string)
print("Is it polidrome?: ", my_string.is_palidrome())

# Створення іншого екземпляру MyString
another_string = MyString("hello")
print("Row: ", another_string)
print("Is it polindrome?: ", another_string.is_palidrome())

# ------------------------------------------------------------------------------------

class TruncatedString(UserString):
    MAX_LEN = 7

    def truncate(self):
        self.data = self.data[:self.MAX_LEN]

ts = TruncatedString('hello world')
ts.truncate()
print(ts)
