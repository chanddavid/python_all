class Add:
    a = 0
    b = 0
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
 
    def calculate(self):
        self.answer = self.num1 + self.num2
        print(f"the sum is: {self.answer}")

obj = Add(2, 3)
obj.calculate()
