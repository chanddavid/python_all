import re

def zero_and_one(s):
    # your code here

    return len(s.replace('01','').replace('10',''))

x=zero_and_one("11101111")
print(x)
