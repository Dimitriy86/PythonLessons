# magic method __repr__

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"
    
point = Point(2, 3)
print(repr(point))

# ---------------------------------------------------------------------------------------

# Magic method __str__

class Human:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Human named {self.name} who is {self.age} years old"
    
    def __repr__(self):
        return f"Human {self.name}, {self.age}"


human = Human("Alice", 30)
print(human)
