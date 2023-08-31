from functools import reduce

l=list(range(1,11))
print(f"list: {l}")

evens = list(filter(lambda n: n % 2 == 0, l))
print(f"evens (l(filter(lambda n: n % 2 == 0, l))): {evens}")

evens_product = reduce(lambda x,y: x * y, evens)
print(f"evens product (reduce(lambda x,y: x * y, evens)): {evens_product}")