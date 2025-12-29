from dataclasses import dataclass

# -----------------------------------------------------------------------------------------

@dataclass
class Rectangle:
    width: int
    height: int

    def area(self) -> int:
        return self.width * self.height

rect1 = Rectangle(10, 5)
rect2 = Rectangle(7, 3)
rect3 = Rectangle(8, 6)

print(f"Square of rectangle 1 is {rect1.area()}")
print(f"Square of rectangle 2 is {rect2.area()}")
print(f"Square of recyangle 3 is {rect3.area()}")

