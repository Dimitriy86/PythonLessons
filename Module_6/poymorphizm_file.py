from typing import Protocol

# ------------------------------------------------------------------------------------

# class Duck:
#     def quack(self):
#         print('Quack, quack!')

# class Person:
#     def quack(self):
#         print("I'm Quacking Like a Duck!")

# def make_it_quack(duck):
#     duck.quack()

# duck = Duck()
# person = Person()

# make_it_quack(duck)
# make_it_quack(person)

# -----------------------------------------------------------------------------------

# class Dog:
#     def speak(self) -> str:
#         return "Woof"

# class Cat:
#     def speak(self) -> str:
#         return "Meow"

# class Robot:
#     def speak(self) -> str:
#         return "Beep boop"

# def make_it_speak(speaker) -> None:
#     print(speaker.speak())

# dog = Dog()
# cat = Cat()
# robot = Robot()
# make_it_speak(dog)
# make_it_speak(cat)
# make_it_speak(robot)

# ------------------------------------------------------------------------------------

class Speaker(Protocol):
    def speak(self) -> str:
        pass

class Dog:
    def speak(self) -> str:
        return "Woof"

class Cat:
    def speak(self) -> str:
        return "Meow"

class Robot:
    def speak(self) -> str:
        return "Beep boop"

def make_it_speak(speaker: Speaker) -> None:
    print(speaker.speak())


dog = Dog()
cat = Cat()
robot = Robot()

make_it_speak(dog)
make_it_speak(cat)
make_it_speak(robot)

# ------------------------------------------------------------------------------------