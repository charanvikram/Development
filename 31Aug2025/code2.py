import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from code1 import factorial

# taking input from the user
number = int(input("Enter a number to compute its factorial: "))

try:
    print(f"The factorial of {number} is {factorial(number)}")
except ValueError as e:
    print(e)


