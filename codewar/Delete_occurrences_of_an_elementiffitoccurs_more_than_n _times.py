arr=[20, 37, 21, 1, 1, 3, 3, 7, 2, 2, 2, 1, 3, 4, 5, 1, 1, 27, 25, 45, 12, 11, 33, 30, 42]
def delete_nth(order,max_e):
    arr1=[]
    # code here
    for i in order:
        if i not in arr1:
            arr1.append(i) 
        else:
            if arr1.count(i)<max_e:
                arr1.append(i)
    print(arr1)
delete_nth(arr,1)