 
from expense_manager import (
    add_expense as add,
    view_expenses as view,
    calculate_total,
    update_expenses,
    get_expenses,
    delete_expense
)

from budget_manager import (
    set_budget,
    get_budget,
    update_budget
)

from data_manager import save_data, load_data


def load_previous_data():
    saved_expenses, saved_budget = load_data()

    update_expenses(saved_expenses)
    update_budget(saved_budget)

    print("Previous data loaded successfully!")


def main():

    while True:

        print("\n====== PERSONAL EXPENSE TRACKER ======")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Total Expenses")
        print("4. Set Monthly Budget")
        print("5. View Remaining Budget")
        print("6. Delete Expense")
        print("7. Exit")


        choice = int(input("Enter your choice: "))

        if choice == 1:
            add()

        elif choice == 2:
            view()

        elif choice == 3:
            calculate_total()

        elif choice == 4:
            set_budget()

        elif choice == 5:

            budget = get_budget()
            total = calculate_total()

            remaining = budget - total

            if remaining < 0:
                print(
                    f"Warning: You are over budget by ₹{abs(remaining)}"
                )
            else:
                print(f"Remaining Budget: ₹{remaining}")

        elif choice == 6:
            delete_expense()

        elif choice == 7:
            save_data(get_expenses(), get_budget())

            print("Exiting the program...")
            print("Thank you for using the Personal Expense Tracker!")

            return

        else:
            print("Invalid choice. Please try again.")


load_previous_data()
main()
