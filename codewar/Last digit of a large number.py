
def last_digit(n1, n2):
  
    num1=n1%100
    num2=n2%100
    print(num1,num2)
    if num1==10 and num2==0:
        return 0
    else:
        res=num1**num2
        print(res)
        num3=res%100
        y=str(num3)
        return (int(y[-1]))

x=last_digit(9,7)
print(x)
