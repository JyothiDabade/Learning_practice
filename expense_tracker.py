import csv
from datetime import datetime

DATA_FILE = "expenses.csv"


class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.monthly_budget = 0.0
        self.load_expenses()

    # ---------------- ADD EXPENSE ----------------

    def add_expense(self):
        print("\n--- Add New Expense ---")

        date = input("Enter date (YYYY-MM-DD): ").strip()
        category = input("Enter category: ").strip()
        amount = input("Enter amount: ").strip()
        description = input("Enter description: ").strip()

        # Validate required fields
        if not date or not category or not amount or not description:
            print("All fields are required. Expense not added.\n")
            return

        # Validate date format
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD.\n")
            return

        # Validate amount
        try:
            amount = float(amount)
        except ValueError:
            print("Invalid amount.\n")
            return

        expense = {
            "date": date,
            "category": category,
            "amount": amount,
            "description": description
        }

        self.expenses.append(expense)
        print("Expense added successfully!\n")

    # ---------------- VIEW EXPENSES ----------------

    def view_expenses(self):
        if not self.expenses:
            print("\nNo expenses to show.\n")
            return

        print("\n--- Expense List ---")

        index = 1   # manual counter instead of enumerate()

        for e in self.expenses:
            # skip incomplete data
            if not all(e.values()):
                print("Skipping incomplete record")
                index += 1
                continue

            print(f"{index}. {e['date']} | {e['category']} | {e['amount']} | {e['description']}")
            index += 1

        print()

    # ---------------- BUDGET ----------------

    def set_budget(self):
        value = input("Enter monthly budget: ").strip()
        try:
            self.monthly_budget = float(value)
            print("Budget set successfully.\n")
        except ValueError:
            print("Invalid budget amount.\n")

    def track_budget(self):
        if self.monthly_budget == 0:
            print("Budget not set yet.\n")
            return

        total = 0.0
        for e in self.expenses:
            total += e["amount"]

        print(f"\nTotal spending: {total}")

        if total > self.monthly_budget:
            print("You have exceeded your budget!\n")
        else:
            remaining = self.monthly_budget - total
            print(f"✔ You have {remaining} left for the month.\n")

    # ---------------- SAVE & LOAD ----------------

    def save_expenses(self):
        with open(DATA_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["date", "category", "amount", "description"])
            writer.writeheader()
            writer.writerows(self.expenses)

        print("Expenses saved to file.\n")

    def load_expenses(self):
        try:
            with open(DATA_FILE, "r", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    row["amount"] = float(row["amount"])
                    self.expenses.append(row)
            print("Previous data loaded.\n")
        except FileNotFoundError:
            print("No saved file found — starting fresh.\n")

    # ---------------- MENU ----------------

    def menu(self):
        while True:
            print("=== Expense Tracker ===")
            print("1. Add Expense")
            print("2. View Expenses")
            print("3. Set Budget")
            print("4. Track Budget")
            print("5. Save & Exit")

            choice = input("Choose option: ").strip()

            if choice == "1":
                self.add_expense()
            elif choice == "2":
                self.view_expenses()
            elif choice == "3":
                self.set_budget()
            elif choice == "4":
                self.track_budget()
            elif choice == "5":
                self.save_expenses()
                print("Goodbye!")
                break
            else:
                print("Invalid choice.\n")


# -------- RUN PROGRAM --------
tracker = ExpenseTracker()
tracker.menu()


