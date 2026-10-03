# Project: Expense Tracker - Installment 3
# Author: Vearne Earluoze R. Rodriguez
# Description: Calculates expenses, tax, grand total, and budget comparisons.

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

item1 = input("First expense? ")
amount1 = float(input("Amount? "))
subtotal += amount1

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))
subtotal += amount2

# Calculations
average = subtotal / 2

tax_percent = float(input("Tax rate %? "))
tax = subtotal * (tax_percent / 100)
total = subtotal + tax

budget = float(input("Your budget? "))
over_budget = total > budget
left = budget - total

# Summary Output
print("-" * 40)
print("SUMMARY")
print(f"{item1}:\t\t${amount1}")
print(f"{item2}:\t\t${amount2}")
print(f"Subtotal:\t${subtotal}")
print(f"Average:\t${average}")
print(f"Tax ({tax_percent}%):\t${tax}")
print(f"Grand total:\t${total}")
print(f"Over budget:\t{over_budget}")
print(f"Left in budget:\t${left}")
print("-" * 40)

# Footer
print(f"Made by: {name} | Installment 3")