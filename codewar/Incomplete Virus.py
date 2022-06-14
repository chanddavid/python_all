
# def incomplete_virus(s):
#     count=0
#     binary = {'0','1'}
#     binary1 = {'0'}
#     binary2 = {'1'}  
#     num1=set(s)
#     if num1==binary:
#         x=int(s, 2)
#         return x
#     else: 
#         for i in range(1,int(s)+1):
#             num1=set(str(i))
#             if num1==binary or num1==binary1 or num1==binary2:
#                 count+=1
#         return count
# x=incomplete_virus('1000000000000000000')
# print(x)


def incomplete_virus(s):
    count=0
    binary = {'0','1'}
    binary1 = {'0'}
    binary2 = {'1'}  
    naline=['0','1']
    num1=set(s)
    if num1==binary:
        x=int(s, 2)
        return x
    else: 
        for i in range(1,int(s)+1):
            j=(str(i))
            if j[0] in naline:                               
                num1=set(str(i))
                if num1==binary or num1==binary1 or num1==binary2:
                    count+=1
        return count

x=incomplete_virus('102')
print(x)





    


