#class method is method that shared among all obj
# it doenst need any obj to be instantiated and it know about class and its attributes and method
#class method without passing parameter
# What is the use of class method and static method in Python?
# A class method can access or modify the class state while a static method can't access or modify it

# class Class_Method:

#     @classmethod     #decorator
#     def myfunc(cls):   #class method
#         print("hello")
    
# obj=Class_Method()
# Class_Method.myfunc()  #calling class method


#class method with  parameter

class Class_Method:
    fp="yes"        #class variable
    @classmethod     #decorator
    def myfunc(cls,r):   #class method
        cls.r=r
        print(f"holiday ? :{cls.fp} and is very {cls.r} ")
       

    
obj=Class_Method()
Class_Method.myfunc("strict")  #calling class method