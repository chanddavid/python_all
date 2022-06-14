class A:
  def fusnction(self):
    print("i am A")

class B(A):
  def func(self):
    print("i am B")
  def function(self):
    print("i am B")

class C(A):
  def func(self):
    print("i am C")

class D(C,B):
  def func(self):
    print("i am D")
  

obj1=D()
obj1.function()

print(D.mro())