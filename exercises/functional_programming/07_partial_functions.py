'''
Exercise 7: Partial Functions

Import the functools module.
Create a function that calculates the power of a number by providing a base and an exponent.
Use the partial() function from the functools module to create a new function that calculates the square of a number using the original function.
Call both the original and the squared functions with sample values.
'''
from functools import partial

def num_power(b,e): 
  return b ** e

square = partial(num_power, e=2)
print("full function: ", num_power(2,3))

print("square with partial: ", square(4))