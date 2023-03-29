from abc import ABC, abstractmethod
from copy import deepcopy

class Shape(ABC):
    def __init__(self):
        pass
    
    def clone(self):
        return self.__class__(**deepcopy(self.__dict__))


class Cicle(Shape):
    def __init__(self, radius: int, color: str):
        self.radius = radius
        self.color = color


class Square(Shape):
    def __init__(self, height: int, width: int, color: str, position: dict):
        self.height = height
        self.width = width
        self.color = color
        self. position = position


position = {"x":1, "y":2}

square_blue = Square(7,5, 'blue', position)
print(square_blue)

square_red = square_blue.clone()
square_red.position['x'] = 3
square_red.color = 'red'
print(square_red)

print(square_blue.__dict__)
print(square_red.__dict__)

