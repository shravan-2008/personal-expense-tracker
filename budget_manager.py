monthly_budget = 0


def set_budget():
    global monthly_budget
    print("Set Monthly Budget")
    monthly_budget = float(input("Enter your monthly budget: "))
    print(f"Monthly budget set to ₹{monthly_budget}")


def get_budget():
    return monthly_budget

def update_budget(saved_budget):
    global monthly_budget
    monthly_budget = saved_budget