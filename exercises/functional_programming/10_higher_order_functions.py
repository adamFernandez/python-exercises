from pprint import pp
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 40},
    # Add more people
]

sorted_by_age = sorted(people, key=lambda person: person["age"])
print("Sorted by age (ascending):")
pp(sorted_by_age)

sorted_by_name_length = sorted(people, key=lambda person: len(person["name"]), reverse=True )
print("Sorted by name length (descending):")
pp(sorted_by_name_length)