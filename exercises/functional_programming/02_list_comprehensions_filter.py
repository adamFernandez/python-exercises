# l=list(range(1,101))
# print(f"list: {l}")
l=[x for x in range(1,101)]
print(f"list: {l}")
even_numbers = list(filter(lambda x: x % 2 == 0, l))
print(f"list(filter(lambda x: x % 2 == 0, l)): {even_numbers}")