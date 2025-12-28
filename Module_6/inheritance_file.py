class Animal:
    def __init__(self, nickname: str, age: int):
        self.nickname = nickname
        self.age = age
    
    def make_sound(self):
        pass

class Cat(Animal):
    def make_sound(self) -> str:
        return "Meow"

class Dog(Animal):
    def make_sound(self) -> str:
        return "Woof"
    
class Cow(Animal):
    def make_sound(self):
        return "Moo"

my_cat = Cat('Simon', 4)
my_dog = Dog('Rex', 5)
my_cow = Cow('Bessie', 3)

print(my_cat.make_sound())
print(my_dog.make_sound())
print(my_cow.make_sound())

# --------------------------------------------------------------------------------------

class Animal:
    def __init__(self, nickname: str, age: int):
        self.nickname = nickname
        self.age = age
    
    def make_sound(self):
        pass

class Cat(Animal):
    def make_sound(self) -> str:
        return "Meow"

class Dog(Animal):
    def __init__(self, nickname: str, age: int, breed: str):
        super().__init__(nickname, age)   # Викликаємо конструктор базового класу
        self.breed = breed
    
    def make_sound(self):
        return "Woof"
    
    def chase_tail(self) -> str:
        return f"{self.nickname} is chasing its tail!"
    
class Cow(Animal):
    def make_sound(self):
        return "Moo"

my_cat = Cat('Simon', 4)
my_dog = Dog('Rex', 5, 'Golden Retriver')
my_cow = Cow('Bessie', 3)

print(my_cat.make_sound())
print(my_dog.make_sound())
print(my_dog.chase_tail())
print(my_cow.make_sound())

# --------------------------------------------------------------------------------------
