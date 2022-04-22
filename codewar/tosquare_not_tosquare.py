import math 
arr=[100, 101, 5, 5, 1, 1]
def square_or_square_root(arr):
    """Return a new array with processing every number of the input-array like this:
    [4,3,9,7,2,1] -> [2,9,3,49,4,1]
        If the number has an integer square root, take this, otherwise square the number.
    Args:
        arr (_type_): array 
    Returns:
        _type_: new array 
    """
    arr1=[]
    for i in arr:
        if math.sqrt(i)%2==0 or math.sqrt(i)%2==1:
           arr1.append(int(math.sqrt(i)))

        elif math.sqrt(i*i)%2==0 or math.sqrt(i*i)%2==1:
            arr1.append(i*i)
    return arr1
x=square_or_square_root(arr)
print(x)
