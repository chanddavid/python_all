import math
# list=[1,34,6,3,87,8,9]
# list=[int(input("enter the list:")) for x in range(1,100)]

import random
#Generate 5 random numbers between 10 and 30
list = random.sample(range(10, 1000), 10)

def mergesort(list):
    
    if len(list)>1:
        mid=math.floor(len(list)/2)

        left=list[:mid]
        right=list[mid:]

        mergesort(left)
        mergesort(right)
        i=0
        j=0
        k=0
        while i<len(left) and j<len(right):

            if left[i]<right[j]:
                list[k]=left[i]
                i+=1
                k+=1

            else:
                list[k]=right[j]
                j+=1
                k+=1

        while i<len(left):
            list[k]=left[i]
            i+=1
            k+=1

        while j<len(right):
            list[k]=right[j]
            j+=1
            k+=1
mergesort(list)
print("sorted list is :",list)