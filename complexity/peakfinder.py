# # arr=[1,23,4,67,10,22,20,45,32]
# arr=[1,23,4,67,30,22,20,45,32]
# start=0
# end=len(arr)-1

# mid=int((start + end )/2);
# # print(arr[mid])
# # print(arr[mid-1])

# if arr[mid]>=arr[mid-1] and arr[mid]>=arr[mid+1]:
#     print("the peak is",+ arr[mid])


# elif arr[mid]<=arr[mid-1] and arr[mid]>=arr[mid+1]:

#     print("the peak is at left side")

#     starts=0
#     ends=arr.index(arr[mid-1])
#     print(starts,ends) #0,3
#     print(arr[0],arr[ends])

#     mids=int((starts + ends)/2)
#     print(arr[mids])

#     if arr[mids]>=arr[mids-1] and arr[mids]>=arr[mids+1]:
#         print("the peak is ",arr[mids])


# array=[10,4,7,12,9,8,19]

# array=[100,4,1,3,9,8,20]

    
def peakfinder(arr,n):
    """this function find the peak element from the given array

    Args:
        arr (array): the array of random number
        n :length of array
    """
    start=0
    end=n-1 

    while(start<=end):
        mid=int((start + end )/2)

        if mid==0 or arr[mid]>=arr[mid-1] and mid==n-1 or arr[mid]>=arr[mid+1]:

            return mid
        elif arr[mid]<=arr[mid+1]:
            end=mid+1
        
        else:
            start=mid-1
    
    return 0