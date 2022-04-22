

def find_multiples(integer, limit):
    """return a number multiple of integer within a given limit

    Args:
        integer (_type_): starting integer
        limit (_type_): end integer

    Returns:
        _type_: list of multiple of t=hat item
    """
    list=[]
    for i in range(integer,limit+1):
        if i%integer==0:
            list.append(i)
            
    return list

x=find_multiples(2, 6)
print(x)