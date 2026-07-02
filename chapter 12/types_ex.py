from typing import List, Tuple, Dict, Union

#List of integers
numbers: List[int] = [2,6,4,8]

#Tuple of a string and an integer
object: Tuple[str, int] = ("fan", 8)

#Dictionary with string keys and integer values
score: Dict[str, int] = {"Janu": 98, "Amu": 90}

# Union type for variables that can hold multiple types
identifier: Union[int, str] = "J8G35"
identifier = 1234

n : int = 5
name : str = "Janu"

def mul(a: int, b: int) -> int:
    return a*b

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
result = mul(a,b)
print("result: ", result)
print(a)