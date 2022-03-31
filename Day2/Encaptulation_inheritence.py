class Employee:
    def __init__(self,name):
        self.__name=name
        # indicate the name is protected
    def get(self):
        print(f"my name is {self.__name}")


class Ram(Employee):
    def getprivate(self):
        print(f"my name is {self.__name}")


obj=Employee("tankman")
print(obj._Employee__name)

obj1=Ram("ram")
obj1.getprivate()
# this above code throw the error
# so how to solve this
