# Project: Expense Tracker - Installment 4
# Author: Vearne Earluoze R. Rodriguez
# Description: Categorizes expense sizes and determines budget verdicts with conditionals.

print("-" * 40)
print("\tEXPENSE TRACKER")
print("\tKnow where your money goes.")
print("=" * 40)

print("MAIN MENU")
print("[1] Add an expense\t\t(coming soon)")
print("[2] View all expenses\t\t(coming soon)")
print("[3] Show total spent\t\t(coming soon)")
print("[4] Exit\t\t\t(coming soon)")
print("=" * 40)

# Input: Name greeting
name = input("What's your name? ")
print(f"Welcome, {name}! Let's log two expenses.")

# Subtotal initialization and incremental accumulation
subtotal = 0.0

# First Expense
item1 = input("First expense? ")
amount1 = float(input("Amount? "))
subtotal += amount1

if amount1 > 200:
    print("  Huge expense — are you sure?")
elif amount1 > 100:
    print("  Big expense.")
elif amount1 > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")

# Second Expense
item2 = input("Second expense? ")
amount2 = float(input("Amount? "))
subtotal += amount2

if amount2 > 200:
    print("  Huge expense — are you sure?")
elif amount2 > 100:
    print("  Big expense.")
elif amount2 > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")

# Two big expenses check
if amount1 > 100 and amount2 > 100:
    print("  Two big expenses in a row — slow down!")

# Calculations
average = subtotal / 2

tax_percent = float(input("Tax rate %? "))
tax = subtotal * (tax_percent / 100)
total = subtotal + tax

budget = float(input("Your budget? "))
over_budget = total > budget

# Summary Output
print("-" * 40)
print("SUMMARY")
print(f"{item1}:\t\t${amount1}")
print(f"{item2}:\t\t${amount2}")
print(f"Subtotal:\t${subtotal}")
print(f"Average:\t${average}")
print(f"Tax ({tax_percent}%):\t${tax}")
print(f"Grand total:\t${total}")

# Budget Verdict
if over_budget:
    over_amount = total - budget
    print(f"Over budget by ${over_amount}!")
elif total > (0.90 * budget):
    left_amount = budget - total
    print(f"Careful: only ${left_amount} left.")
else:
    left_amount = budget - total
    print(f"Within budget. ${left_amount} left.")

print("-" * 40)

# Footer
print(f"Made by: {name} | Installment 4")