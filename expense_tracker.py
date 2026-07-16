expenses = []

while True:
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. Show Total")
    print("3. Show All Expenses")
    print("4. Exit")
    gi

    choice = input("Enter choice: ")

    if choice == "1":
        amount = float(input("Enter expense amount: "))
        expenses.append(amount)
        print("Expense added")

    elif choice == "2":
        print("Total Expense:", sum(expenses))

    elif choice == "3":
        print("All Expenses:", expenses)

    elif choice == "4":
        print("Exiting...")
        break

    else:1

        print("Invalid choice")