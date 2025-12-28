class Animal:
    def __init__(self, nickname: str, age: int):
        self.nickname = nickname
        self.age = age

    def make_sound(self):
        pass

class Bird(Animal):
    def make_sound(self):
        return "Chirp"

class Parrot(Bird):
    def can_fly(self):
        return True

class TalkingParrot(Parrot):
    def say_phrase(self, phrase):
        return f"The parrot says: {phrase}"

my_parrot = TalkingParrot('Alice', 2)
print(my_parrot.make_sound())
print(my_parrot.can_fly())
print(my_parrot.say_phrase('Hello, world!'))

# ------------------------------------------------------------------------------------

    # Method Resolution Order
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

print(D.mro())  # Виведе порядок розв'язання методів для класу D

# ------------------------------------------------------------------------------------

class A:
    name = 'I am a class A'

class B:
    name = 'I am a class B'
    property = 'I am in a class B'

class C(A, B):
    property = 'I am in a class C'

c = C()
print(c.name)
print(c.property)
