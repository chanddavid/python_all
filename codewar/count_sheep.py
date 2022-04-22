
n=2
def count_sheep(n):
    """this function return a number of sheep according to n

    Args:
        n (_type_): number
    """
    # return ''.join(f"{i} sheep..." for i in range(1,n+1))
    x=""
    # your code
    value="sheep..."
    for i in range(1,n+1):     
        if i>=1:
            x=x+(str(i)+' '+value)        
    # return x
x=count_sheep(n)
print(x)
