l=list(range(1,11))
print(f"list: {l}")
new_list=list(map(lambda n: n*n, l))
print(f"list(map(lambda n: n*n, l)): {new_list}")