num = 9119

squared = list(map(lambda x: int(x) **2, str(num)))
print(squared)
to_number = int("".join(map(str, squared)))
print(to_number)

def square_digits(num):
    return int(''.join(str(int(d)**2) for d in str(num)))

print(square_digits(num))