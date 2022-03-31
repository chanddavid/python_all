# class Static_Method:
#     id=5
#     def get():
#         print(f"my id id {Static_Method.id}")

# obj=Static_Method()
# Static_Method.get()


class Static_Method:
    @staticmethod
    def get(n,r):
        name=n
        roll=r
        print(f"my name is {name} and roll is {roll}")

obj=Static_Method()
Static_Method.get("tankman",15)