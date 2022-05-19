


special_char="""#$%&'(!) *+,-./:;"<=>?@[\]^_`{|}~"""
number='1234567890'
upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower='abcdefghijklmnopqrstuvwxyz'



def solve(s):
    count_u=0
    count_l=0
    count_n=0
    count_s=0

    for i in s:
        if i in special_char:
            count_s+=1
        elif i in number:
            count_n+=1
        elif i in upper:
            count_u+=1
        elif i in lower:
            count_l+=1
    x=count_u,count_l,count_n,count_s
    ans=list(map(int, x))
    return (ans)

x=solve("#!""$ %&'()*+,-./:;<=>?@[\]^_`{|}~")
print(x)
