# Project: Expense Tracker - Installment 5
# Author: Vearne Earluoze R. Rodriguez
# Description: Implements an interactive loop menu to log expenses, view totals, and exit cleanly.

# Banner (prints once at startup)
print("-" * 40)
print("\tEXPENSE TRACKER")
print("\tKnow where your money goes.")
print("=" * 40)

# Setup questions (asked once per run)
name = input("What's your name? ")
tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))

print(f"Welcome, {name}!")

# State trackers
subtotal = 0.0
count = 0

# Interactive Menu Loop
while True:
    print("=" * 40)
    print("MAIN MENU")
    print("[1] Add an expense")
    print("[2] View all expenses (coming soon)")
    print("[3] Show total spent")
    print("[4] Exit")
    print("=" * 40)

    choice = input("Choose 1-4: ")

    if choice == "1":
        amount = float(input("Amount? "))
        subtotal += amount
        count += 1

        if amount > 200:
            print("  Huge expense — are you sure?")
        elif amount > 100:
            print("  Big expense.")
        elif amount > 50:
            print("  Moderate expense.")
        else:
            print("  Small expense.")

    elif choice == "2":
        print("Coming soon: the tracker can't remember each item yet.")

    elif choice == "3":
        tax = subtotal * (tax_percent / 100)
        total = subtotal + tax

        print(f"Expenses:\t{count}")
        print(f"Subtotal:\t${subtotal}")
        print(f"Tax ({tax_percent}%):\t${tax}")
        print(f"Grand total:\t${total}")

        if total > budget:
            over_amount = total - budget
            print(f"Over budget by ${over_amount}!")
        elif total > (0.90 * budget):
            left_amount = budget - total
            print(f"Careful: only ${left_amount} left.")
        else:
            left_amount = budget - total
            print(f"Within budget. ${left_amount} left.")

    elif choice == "4":
        print(f"Goodbye, {name}!")
        print("-" * 40)
        print(f"Made by: {name} | Installment 5")
        break

    else:
        print("Please choose 1, 2, 3 or 4.")