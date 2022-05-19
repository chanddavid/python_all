
x="1234"
print(x[:2])

def delete_digit(n):
    x=str(n)
    newlist=[]
    
    for i in range(len(x)):
        
        num=x[:i]+x[1+i:]
        newlist.append(num)
        
    print(max(newlist))

delete_digit(100001)


