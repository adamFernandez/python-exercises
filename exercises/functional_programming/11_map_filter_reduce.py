from functools import reduce

'''
Create a list of numbers.
Use the map() function to square each number in the list.
Use the filter() function to keep only the even numbers from the squared list.
Use the reduce() function to calculate the product of the even numbers.
'''

numbers = list(range(1,11))
# print(numbers)

squared = list(map(lambda x: x ** 2, numbers))
print("squared: ", squared)

even = list(filter(lambda x: x % 2 == 0, squared))
print("even from squared: ", even)

product = reduce(lambda a,x: a * x,even)
print("product from even: ", product)
