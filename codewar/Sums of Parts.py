
# def parts_sums(ls):
#     total = sum(ls)
#     count = 0
#     newarr = []
#     for i in range(len(ls)):
#         if len(newarr) == 0:
#             newarr.append(total)
#         else:
#             newarr.append(total - count)
#         count += ls[i]
#     newarr.append(0)
#     return newarr
# x=parts_sums([0, 1, 3, 6, 10])
# print(x)





def parts_sums(ls):
    newarr = [sum(ls)]
    for i in range(len(ls)):
        x=newarr[i]-ls[i]
        newarr.append(x)
    return newarr
x=parts_sums([0, 1, 3, 6, 10])
print(x)
