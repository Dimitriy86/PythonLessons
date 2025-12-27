class User:
    name = 'Anonymnous'
    age = 15

user1 = User()
print(user1.name)
print(user1.age)

user2 = User()
user2.name = 'John'
user2.age = 90

print(user2.name)
print(user2.age)

# --------------------------------------------------------------------------------

class MyClass:
    def __init__(self, value):
        self.instance_field = value     # Поле класу

obj1 = MyClass(5)
obj2 = MyClass(10)

print(obj1.instance_field, obj2.instance_field)

# --------------------------------------------------------------------------------

class Person:
    def __init__(self, name: str, age:int):
        self.name = name
        self.age = age
    
    def say_name(self) -> None:
        print(f'Hi! I am {self.name} and I am {self.age} years old.')
    
    def set_age(self, age: int) -> None:
        self.age = age

bob = Person('Bob', 34)

bob.say_name()
bob.set_age(25)
bob.say_name()

# --------------------------------------------------------------------------------

class Person:
    count = 0


    def __init__(self, name: str):
        self.name = name
        Person.count += 1
    
    
    def how_many_persons(self):
        print(f"The number of people is currently {Person.count}")


first = Person('Boris')
first.how_many_persons()

second = Person('Alex')
first.how_many_persons()

# --------------------------------------------------------------------------------

class Person:
    count = 0

    def __init__(self):
        pass

person = Person()
print(person.count)

# --------------------------------------------------------------------------------

class Person:
    count = 0

    def __init__(self):
        self.count = 10


person = Person()
print(person.count)
print(Person.count)

# --------------------------------------------------------------------------------

class Pokemon:
    def __init__(self, name, type, health):
        self.name = name
        self.type = type
        self.health = health
    
    def attack(self, other_pokemon):
        print(f"{self.name} attacks {other_pokemon.name}!")
    
    def dodge(self):
        print(f"{self.name} dodged the attack!")
    
    def evolve(self, new_form):
        print(f"{self.name} is evolving into {new_form}!")
        self.name = new_form

# Створення об'єкта Pikachu
pikachu = Pokemon('Pikachu', 'Electric', 100)

# Використання методів
pikachu.attack(Pokemon("Charmander", "Fire", 100))
pikachu.dodge()
pikachu.evolve("Raichu")

# --------------------------------------------------------------------------------

