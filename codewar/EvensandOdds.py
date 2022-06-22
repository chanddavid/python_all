def evens_and_odds(n):
    #your code here
    if n%2==0:
        return bin(n)[2:]  
    else:
        return hex(n)[2:]
x=evens_and_odds(13)
print(x)
