# # binary search
# # list=[1,5,7,2,9,8]
# # list.sort()
list=[]
n=int(input("enter a number to search: "))
start=0
for i in range(1,10):
    list.append(i)
end=len(list)-1
def func(list,n,start,end):
    """function that search a number in array using binary search
    Args:
        list (_type_): list
        n (_type_): number u want to search
    """  
    while start>end:  
        return False
    mid=int((start + end )/2)   
    if list[mid]==n:        
        return True
    elif list[mid]>n:
        return func(list,n,start,mid-1)       
    else:
        return func(list,n,mid+1,end)
x=func(list,n,start,end)
print(x)

# list=[]
# n=n=int(input("enter a number to search: "))
# for i in range(1,10000000):
#      list.append(i)
# print(n in list)