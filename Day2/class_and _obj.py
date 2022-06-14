# class form:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
     
#     def func(self):
#         print(f"my name is {self.name}")
#         print(f"my age is {self.age}")

# obj=form("tankman",16)
# obj.func()



class form:
    roll=20
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def func(self):
        print(f"my name is {self.name}")
        print(f"my age is {self.age}")

obj=form("tankman",16)
obj.roll=23
print(obj.roll)
