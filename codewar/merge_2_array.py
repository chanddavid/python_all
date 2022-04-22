arr1=[1,1,2,3,4,4,5,6,7]
arr2= [4,65,8]
def merge_arrays(arr1, arr2):
    """merge two sorted array into one
    Args:
        arr1 (_type_): array 1
        arr2 (_type_): array 2
    Returns:
        _type_: sorted one array
    """
    arr=[]
    arr3=arr1+arr2
    arr3.sort()
    for i in arr3:
        if not i in arr:
            arr.append(i)     
    return arr   
x=merge_arrays(arr1, arr2)
print(x)



# def merge_arrays(arr1, arr2):
#     return sorted(set(arr1+arr2))