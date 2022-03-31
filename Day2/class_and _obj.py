class form:
    def func(self):
        print(f"my name is {self.name}")
        print(f"my age is {self.age}")

obj=form()
obj.name="tankman"
obj.age=23
obj.func()