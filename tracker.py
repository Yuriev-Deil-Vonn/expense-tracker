# Project: Expense Tracker - Installment 2
# Author: Vearne Earluoze R. Rodriguez
# Description: Takes user input for expenses and displays a formatted summary.

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

# Input: Name greeting and expenses
name = input("What's your name? ")
print(f"Welcome, {name}! Let's log two expenses.")

item1 = input("First expense? ")
amount1 = float(input("Amount? "))

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))

# Calculations
total = amount1 + amount2
average = total / 2

# Summary Output
print("-" * 40)
print("SUMMARY")
print(f"{item1 + ':':<16}${amount1}")
print(f"{item2 + ':':<16}${amount2}")
print(f"{'Total spent:':<16}${total}")
print(f"{'Average:':<16}${average}")
print("-" * 40)

# Footer
print(f"Made by: {name} | Installment 2")