lst = [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]
def move_zeros(lst):
    for i in lst:
        if i==0:
            index = lst.index(i)
            move = lst.pop(index)
    return lst

print(move_zeros(lst))


def move_zeros(array):
    for i in array:
        if i == 0:
            array.remove(i) # Remove the element from the array
            array.append(i) # Append the element to the end
    return array


def move_zeros(array):
    return sorted(array, key=lambda x: x==0 and type(x) is not bool)