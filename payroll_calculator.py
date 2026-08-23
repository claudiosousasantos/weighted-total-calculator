def calculate_payroll_total(salary_components, bonus_rate):
    subtotal = sum(salary_components)
    total = subtotal + (subtotal * bonus_rate)
    return total

# Example: an employee's base salary components
salary_components = [3000.00, 500.00, 250.00]  # e.g., base pay, allowances, overtime
bonus_rate = 0.10  # 10% performance bonus/commission

total_pay = calculate_payroll_total(salary_components, bonus_rate)
print(f"The total payroll amount (including bonus) is: ${total_pay:.2f}")