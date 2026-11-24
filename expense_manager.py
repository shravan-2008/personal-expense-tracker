from datetime import date

expenses = []

def add_expense():
    print("\n===== ADD EXPENSE =====")

    while True:
        try:
            amount = float(input("Enter expense amount: "))

            if amount <= 0:
                print("Amount must be greater than zero.")
                continue

            break

        except ValueError:
            print("Invalid input. Please enter a valid number.")

    category = input("Enter expense category: ")
    expense_date = date.today()

    expense = {
    "amount": amount,
    "category": category,
    "date": str(expense_date)
    }

    expenses.append(expense)

    print("\nExpense added successfully!")


def view_expenses():
    if not expenses:
        print("No expenses recorded.")

    else:
        print("\n===== ALL EXPENSES =====")

        for index, expense in enumerate(expenses, start=1):
            print(f"\nExpense No: {index}")
            print(f"Amount: ₹{expense['amount']}")
            print(f"Category: {expense['category']}")
            print(f"Date: {expense.get('date', 'Not available')}")
            print("-------------------------")



def calculate_total():
    if not expenses:
        print("No expenses recorded.")
        return 0

    else:
        total_expense = 0

        for expense in expenses:
            total_expense += expense["amount"]
            
        print("\n===== EXPENSE SUMMARY =====")
        print(f"Total Entries: {len(expenses)}")
        print(f"Total Expense Amount: ₹{total_expense}")

        return total_expense

def update_expenses(saved_expenses):
    global expenses
    expenses = saved_expenses


def get_expenses():
    return expenses

def delete_expense():
    if not expenses:
        print("No expenses available to delete.")
        return

    print("\n===== DELETE EXPENSE =====")

    for index, expense in enumerate(expenses, start=1):
        print(f"\n{index}. Amount: ₹{expense['amount']}")
        print(f"   Category: {expense['category']}")
        print(f"   Date: {expense.get('date', 'Not available')}")

    while True:
        try:
            choice = int(input("\nEnter expense number to delete: "))

            if choice < 1 or choice > len(expenses):
                print("Invalid expense number. Try again.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    deleted_expense = expenses.pop(choice - 1)

    print("\nExpense deleted successfully!")
    print(f"Deleted Amount: ₹{deleted_expense['amount']}")
    print(f"Deleted Category: {deleted_expense['category']}")