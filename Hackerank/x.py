from decimal import Decimal
from tokenize import Octnumber
from unicodedata import decimal
from sqlalchemy import DECIMAL


def print_formatted(number):
    # your code goes here
    for i in range(1,number+1):
        print(i,oct(i).lstrip("0o").rstrip("L"),hex(i).lstrip("0x").rstrip("L"),bin(i).replace('0b',''))
        print(type(hex(i).lstrip("0x").rstrip("L")))
       
    
       


print_formatted(17)