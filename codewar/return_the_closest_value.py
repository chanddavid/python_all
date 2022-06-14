

def closest_value(arr,value):
    newarr=[]
    for i in arr:
        distance=abs(i-value)
        newarr.append(distance)
    result=min(newarr)
    mindistanceindex=newarr.index(result)

    print(arr[mindistanceindex])

closest_value([10,100,150,200,240],126)

