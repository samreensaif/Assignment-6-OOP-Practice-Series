from abc import ABC, abstractmethod

# Abstract class Shape
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Subclass Rectangle that implements the area method
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Example of using the Rectangle class
rect = Rectangle(15, 10)
print(f"Area of rectangle: {rect.area()}")  # Output will be 50
