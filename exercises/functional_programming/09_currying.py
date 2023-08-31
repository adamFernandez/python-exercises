def calculate_total_costs(quantity):
  def calculate(price):
    return quantity * price
  return calculate

total_cost_5 = calculate_total_costs(5)
total_cost_10 = calculate_total_costs(10)

print(f"total costs for quantity 5 and price 10: {total_cost_5(10)}")
print(f"total costs for quantity 10 and price 20: {total_cost_5(20)}")