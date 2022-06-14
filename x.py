
from tomlkit import value


dict = {
    "1st": {
        "name": "david",
        "age": 30,
        "address": "tikapur"
    },
    "2nd": {
        "name": "rohan",
        "age": 20,
        "address": "ktm"}
}


def fub(dict):
    for key,value in dict.items():
        for key,value in value.items():
            print(f"my name is {value} and {value} years old. i am from {value}")



fub(dict)
