import re 
def remove_parentheses(s):
    pass
    x=re.sub("[\(\[].*?[\)\]]", "", s)
    print(x)


remove_parentheses("example(unwanted thing)example")

# def remove_parentheses(s):
#     if s.find('(') == -1 or s.find(')') == -1: return s
#     else :
#         i=s.rindex('(')
#         j=s[i+1:].index(')')
#         return remove_parentheses(s[:i] + s[i+1+j+1:])  

# remove_parentheses("example(unwanted thing)example")






# import math
# def maths(arr):
#     new=[]
#     length=len(arr)

#     if length==1:
#         print(arr)
    
    
#     prod=math.prod(arr)
#     for i in arr:
#         x=prod//i
#         new.append(x)
#     print(new)
            
# maths([1,2,3,4])