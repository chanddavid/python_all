
from dataclasses import dataclass

@dataclass
class School:
    name:str
    address:str
    code:int    

    def func(self,name):
        return f'my name is {self.name}'

obj1=School("united","tkp",4564)
obj2=School("nirankari","tikapur",2334)
obj3=School("nirankari","tikapur",2334)

print(obj1.func("united"))

