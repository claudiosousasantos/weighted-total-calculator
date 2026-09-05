# Weighted Total Calculator

A reusable Python pattern for summing a list of values and applying a percentage on top, shown across three examples.

## Files
- **order_calculator.py** — order total with tax applied
- **payroll_calculator.py** — payroll total with a bonus/commission applied
- **restaurant_bill.py** — restaurant bill total with tip applied

## How it works
- Takes a list of values and sums them for the subtotal
- Applies a percentage rate (tax, bonus, tip, etc.) to the subtotal
- Returns the final total (subtotal + percentage amount)

## How to run
```bash
python order_calculator.py
python payroll_calculator.py
python restaurant_bill.py
```

## What I learned
- Writing a reusable function with parameters for a list and a rate
- Using Python's built-in `sum()` on a list
- Recognizing the same "sum + percentage" pattern applies across different contexts (retail tax, payroll bonuses, restaurant tips)
