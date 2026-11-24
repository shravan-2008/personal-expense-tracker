import json


def save_data(expenses, budget):

    data = {
        "expenses": expenses,
        "monthly_budget": budget
    }

    with open("expenses.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Data saved successfully!")


def load_data():

    try:
        with open("expenses.json", "r") as file:
            data = json.load(file)

        expenses = data["expenses"]
        budget = data["monthly_budget"]

        return expenses, budget

    except FileNotFoundError:
        return [], 0

 