
def flip(d, a):
    # return sorted(a) if d == 'R' else sorted(a, reverse=True)
    """sorted the list according to the given distance
    Args:
        d (_type_): distance either left or right
        a (_type_): _description_
    Returns:
        _type_: retern sorted list 
    """
    if d=='R':
        return sorted(a)
    else:
        return sorted(a,reverse=True)
x=flip('L', [1, 4, 5, 3, 5])
print(x)