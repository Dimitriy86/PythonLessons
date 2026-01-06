class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.area() == other.area()
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __lt__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.area() < other.area()
    
    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)
    
    def __gt__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.area() > other.area()
    
    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)
    

if __name__ == "__main__":
    rect1 = Rectangle(5, 10)
    rect2 = Rectangle(3, 20)
    rect3 = Rectangle(5, 10)

    print(f"Area of rectangle is: {rect1.area()}, {rect2.area()}, {rect3.area()}")
    print(rect1 == rect3)   # True: areas are equal
    print(rect1 != rect2)   # True: areas are not equal
    print(rect1 < rect2)    # True: the area of rect1 is smaller than the area od rect2
    print(rect1 <= rect3)   # True: areas are equal< than rect1 <= rect2
    print(rect1 > rect2)    # False: the area of rect1 is smaller than the area of rect2
    print(rect1 >= rect3)   # True: areas are equal than rect2 >= rect3

    # -----------------------------------------------------------------------------------------

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __lt__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x < other.x and self.y < other.y
           
    def __gt__(self, other):
        if not isinstance(other, Point):
            NotImplemented
        return self.x > other.x and self.y > other.y
    
    def __le__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x <= other.x and self.y <= other.y

    def __ge__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x >= other.x and self.y >= other.y


if __name__ == "__main__":
    print(Point(0, 0) == Point(0, 0))   # True
    print(Point(0, 0) != Point(0, 0))   # False
    print(Point(0, 0) < Point(1, 0))    # False
    print(Point(0, 0) > Point(0, 1))    # False
    print(Point(0, 2) >= Point(0, 1))   # False
    print(Point(0, 0) <= Point(0, 0))   # True
