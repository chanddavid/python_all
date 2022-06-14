class A:
    def __init__(self,name,age,):
        self.name=name
        self.age=age
    
class B(A):
    def __init__(self, name, age,address,*args,**kwargs):
        super().__init__(name, age)
        self.address=address
        self.args=args
        self.kwargs=kwargs
    
    def info(self):
        for key,value in kwargs.items():
            print(f"my name is {key} and {value} years old")

        print('\n')
        for i in args:
            print(f"my name is {i} and {self.age} years old. i am from {self.address}")

obj=A("tanka",30)
args=["david","ram","hari"]

kwargs={
        "ram": 30,
        "hari": 40,
        "sam": 23
    }
obj2=B("tanka",12,"tikapur",*args,**kwargs)
print(obj2.info())

