# Order Total Calculator

A simple Python script that calculates the total cost of an order, including tax, from a list of item prices.

## How it works
- Takes a list of item prices and sums them for the subtotal
- Applies a tax rate to the subtotal
- Returns the final total (subtotal + tax)

## How to run
```bash
python order_calculator.py
```
The script currently uses a sample order (3 items) and a 7% tax rate. Edit the `order_prices` and `tax` variables to test different values.

## What I learned
- Writing a reusable function with parameters (`item_prices`, `tax_rate`)
- Using Python's built-in `sum()` on a list
- Formatting currency output with f-strings (`:.2f`)
