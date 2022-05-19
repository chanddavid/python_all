def cycle(n) :
    res=""
    rem=1%n
    mp={}
    while ((rem != 0) and (rem not in mp)):
 

        mp[rem] = len(res)
 
        rem = rem * 10
 
        res_part = rem // n
        res += str(res_part)

        rem = rem % n
   
     
 
    if (rem == 0 or rem>=10):
        print(-1) 
    else:
        print(res[mp[rem]:])
    # return(len(x))

cycle(9058)
