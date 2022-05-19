
def open_or_senior(data):
    arr=[]
    j=0
    # return ['Senior' if i[j]>=55 and i[j+1]>7 else 'Open' for i in data ]

    for i in data:
        if i[j]>=55 and i[j+1]>7:
            arr.append('Senior')
        else:
            arr.append('Open')
    return arr

x=open_or_senior([[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]])
print(x)
