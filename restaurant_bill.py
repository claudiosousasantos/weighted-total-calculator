def calculate_bill_total(meal_item_costs, tip_rate):
    subtotal = sum(meal_item_costs)
    total = subtotal + (subtotal * tip_rate)
    return total

# Example: items ordered at a restaurant
meal_items = [24.99, 18.50, 12.75]  # e.g., main course, appetizer, drink
tip = 0.15  # 15% tip
bill_total = calculate_bill_total(meal_items, tip)
print(f"The total bill (including tip) is: ${bill_total:.2f}")