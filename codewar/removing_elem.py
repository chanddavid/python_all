
my_list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def remove_every_other(my_list):
    """remove next item in a list
    Args:
        my_list (_type_): given list
    Returns:
        _type_: list where next item is removed
    """
    list=[]
    for index,letter in enumerate(my_list):
        if index%2==0:
            list.append(my_list[index])            
    return list
x=remove_every_other(my_list)
print(x)

