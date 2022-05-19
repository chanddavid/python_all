from sympy import false, true
from tomlkit import string


string="apple"
ending=""
def solution(string, ending):
    # your code here...
    if string.endswith(ending):
        return true
    else:
        return false
x=solution(string,ending)
print(x)