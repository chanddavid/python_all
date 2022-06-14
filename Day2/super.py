# super function is used to give access to the constructor methods of parents class.
# returns a temporary object of a parents class when used.



class ParentClass:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    

class Child1(ParentClass):
    def __init__(self,name,age,address):
        super().__init__(name,age)
        self.address=address

    def func(self):
        print("Child1 self: ", self)
        print(f"i am {self.name} and {self.age} years old . my roll no is {self.address}")


obj=ParentClass("tanka",23)

obj2=Child1("ram",23,"tikapur")
print(obj2.func())






