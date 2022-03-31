class Ram:
  def about(self):
    print("This the  ram.")

class Hari:
  def about(self):
    print("This the  hari.")

obj1 = Ram()
obj2 = Hari()
for car in (obj1,obj2):
 car.about()