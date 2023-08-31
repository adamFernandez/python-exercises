'''
Create a list of sales transactions, where each transaction is represented as a dictionary.
Use the map() function to calculate the total price for each transaction by multiplying the "quantity" and "price" values.
Use the filter() function to filter out transactions with a total price above a certain threshold.
Use the reduce() function to find the total revenue from the filtered transactions.
Use a list comprehension to extract the names of products from the remaining transactions.
Print the original list of transactions, the filtered transactions, the total revenue, and the list of product names.
'''

from functools import reduce

transactions = [
    {"product": "item1", "quantity": 5, "price": 10},
    {"product": "item2", "quantity": 3, "price": 25},
    {"product": "item3", "quantity": 8, "price": 15},
    {"product": "item4", "quantity": 7, "price": 2},
    {"product": "item5", "quantity": 2, "price": 50},
    {"product": "item6", "quantity": 1, "price": 12},
    {"product": "item7", "quantity": 5, "price": 5},
    # Add more transactions
]

total_price = list(map(lambda t: t["quantity"] * t["price"], transactions))

print("Total price: ", total_price)

threshold = 50
below_50 = list(filter(lambda t: t["quantity"] * t["price"] <= threshold, transactions))

print("Below 50: ", below_50)


total_below_50 = reduce(lambda t, tx: t + tx["quantity"] * tx["price"], below_50, 0)
print("Total below 50: ", total_below_50)


below_50_names = [n["product"] for n in below_50]
print(f"Below 50 product names: {below_50_names}")