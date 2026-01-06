class Person:
    def __init__(self, age):
        self.__age = None    # Пряме присвоєння значення атрибуту в конструкторі
        # Використовуємо сеттер для встановлення віку, що дозволяє валідацію вхідного значення
        self.age = age
    
    @property
    def age(self):
        return self.__age   # Геттер повертає значення приватного поля
    
    @age.setter
    def age(self, value):
        if value < 0:
            # Валідація вхідного значення
            raise ValueError('Age cannot be less than zero.')
        # Присвоєння валідного значення приватному полю
        self.__age = value

if __name__ == "__main__":
    person = Person(-10)
    print(person.age)
    person.age = -5

# ---------------------------------------------------------------------------------------

class Person:
    def __init__(self, name: str, age: int, is_active: bool, is_admin: bool):
        self.name = name
        self.age = age
        self._is_active = None
        self.__is_admin = None
        self._is_active = is_active
        self.__is_admin = is_admin

    
    @property
    def is_active(self):
        return self._is_active
    
    @is_active.setter
    def is_active(self, value: bool):
        # Тут можна додати буть-яку логіку перевірки фбо обробки
        self._is_active = value

    @property
    def is_admin(self):
        return self.__is_admin
    
    @is_admin.setter
    def is_admin(self, value):
        # Тут можна додати будь-яку логіку перевірки фбо обробки
        self.__is_admin = value

    def greeting(self):
        return f"Hi {self.name}"


if __name__ == "__main__":
    person = Person('Boris', 34, True, False)
    print(person.is_admin)      # Виконуємо геттер
    person.is_admin = True      # Виконуємо сеттер
    print(person.is_admin)
    