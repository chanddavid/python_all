# class Singleton:
#    __instance = None
#    @staticmethod 
#    def getInstance(a):
#       print("get instance")
#       if Singleton.__instance == None:
#          Singleton(a)
#       return Singleton.__instance
#    def __init__(self,a):
#       print(" Virtually private constructor.")
#       if Singleton.__instance != None:
#         print("if")
#         raise Exception("This class is a singleton!")
#       else:
#         print("else")
#         Singleton.__instance = self

# s = Singleton.getInstance(1)
# print(s)

# t = Singleton.getInstance(12)
# print(t)



from dataclasses import dataclass

@dataclass
class Singleton:
   __instance = None
   name:str
   age:int  

   @staticmethod 
   def getInstance(a,b):
      print("get instance")
      if Singleton.__instance == None:
         Singleton(a,b)
      return Singleton.__instance

s = Singleton.getInstance("ram",12)
print(id(s))

t = Singleton.getInstance("hari",14)
print(id(t))



