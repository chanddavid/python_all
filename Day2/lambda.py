'''ambda expression-is a breakdown of function into one line,used when you want to use function only 
      one time and it return a value'''

x=lambda a,b: a*b
res=x(5,3)
print(res)



def add(a):
    return lambda x:x*a
ans=add(2)
result=ans(3)
print(result)