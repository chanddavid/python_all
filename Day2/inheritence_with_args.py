class Company:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def power(self):
        print(f"this is {self.name} company and is {self.age} year old")


class Employee(Company):

    def sal(self,ename,salary):
        print(f'the name is {ename} and salary is {salary} and from {self.name} company')


comp=Company('ekbana',12)
comp.power()

emp=Employee("Ekbana",10)
emp.sal("tankman",300000)