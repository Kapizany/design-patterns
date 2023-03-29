class Monostate:
    __shared_state = {}
    def __init__(self):
        self.__dict__ = self.__shared_state

obj_1 = Monostate()
print(obj_1)
obj_2 = Monostate()
print(obj_2)

obj_1.x = "teste"

print(obj_1.__dict__)
print(obj_2.__dict__)
