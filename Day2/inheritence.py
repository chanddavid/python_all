class Employee:
    company="ekbana"
    def detail(self):
        print(f"this is {self.company} company")
    
class Program(Employee):
    lang="python"
    def showdetail(self):
        print(f"this is {self.lang} langauge and learning in {self.company}")
    
class Subject(Program):
    def sub(self):
        print(f"this is last class and main class is {self.company}")

e=Employee()
e.detail()

p=Program()
p.showdetail()

o=Subject()
o.sub()

o.showdetail()
o.detail()

