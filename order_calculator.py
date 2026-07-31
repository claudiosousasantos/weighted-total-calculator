def calcute_total(item_prices, tax_rate):
    subtotal = sum(item_prices)
    total = subtotal + (subtotal * tax_rate)
    return total

order_prices = [10.99, 5.49, 3.99]
tax = 0.07
total_cost = calcute_total(order_prices, tax)
print(f"The total cost of the order is: ${total_cost:.2f}")