from abc import ABC, abstractmethod
from copy import deepcopy

"""
    Exemple taken from https://refactoring.guru/design-patterns/builder
"""

class House:
    def __init__(self):
        self._walls = None
        self._doors = None
        self._windows = None
        self._roof = None
    
    @property
    def walls(self):
        return self._walls
    
    @walls.setter
    def walls(self, value:int):
        self._walls = value
    
    @property
    def doors(self):
        return self._doors
    
    @doors.setter
    def doors(self, value:int):
        self._doors = value
    
    @property
    def windows(self):
        return self._windows
    
    @windows.setter
    def windows(self, value:int):
        self._windows = value
    
    @property
    def roof(self):
        return self._roof
    
    @roof.setter
    def roof(self, value:str):
        self._roof = value
        
        

class Builder(ABC):
    @abstractmethod
    def reset(self):
        pass
    
    @abstractmethod
    def build_walls(self, num: int):
        pass
    
    @abstractmethod    
    def build_doors(self, num: int):
        pass
    
    @abstractmethod    
    def build_windows(self, num: int):
        pass
    
    @abstractmethod    
    def build_roof(self, shape: str):
        pass
    
    @abstractmethod    
    def get_result(self):
        pass
    

class HouseBuilder(Builder):

    def  __init__(self):
        self.reset()

    def reset(self):
        self._house = House()

    def build_walls(self, num: int):
        self._house.walls = num
        
    def build_doors(self, num: int):
        self._house.doors = num
        
    def build_windows(self, num: int):
        self._house.windows = num
        
    def build_roof(self, shape: str):
        self._house.roof = shape

    def get_result(self) -> House:
        product = deepcopy(self._house)
        self.reset()
        return product

class Director:
    def construct_regular_home(self, builder:HouseBuilder):
        builder.reset()
        builder.build_doors(2)
        builder.build_walls(4)
        builder.build_windows(2)
        builder.build_roof("triangular")
        return builder.get_result()
    
    def construct_home_with_garage(self):
        pass
    
    def construct_castle(self):
        pass

director = Director()
builder = HouseBuilder()
print(director.construct_regular_home(builder).__dict__)