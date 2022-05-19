

bing=[2,9,14,7,15]
arr=[2,9,14,15,1, 2, 3, 5, 14, 15, 9, 10]
def bingo(arr): 
    x=[]
    for i in bing:       
        if i in arr:
            x.append(i)

    if x==bing:
        return "WIN"
    else:
        return "LOSE"
x=bingo(arr)
print(x)


# def bingo(arr): 
#     # your code here
#     return "WIN" if {2,9,14,7,15}.issubset(arr) else "LOSE"
# x=bingo([2,9,14,15,1, 7,2, 3, 5, 14, 15, 9, 10])
# print(x)

