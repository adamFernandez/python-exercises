def row_sum_odd_numbers(n):
    first = n * (n - 1) + 1
    last = first + 2 * (n - 1)
    row = (first + last) * n // 2
    return row


n =3
first= n * (n -1 ) + 1
print(first)
last= first + 2 * (n -1)
print(last)
row = (first + last) * n // 2
print(row)

# Best solution:
def n_row_odd_triangle(n):
  n ** 3