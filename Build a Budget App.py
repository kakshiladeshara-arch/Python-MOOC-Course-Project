import math

class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            desc = item["description"][:23]
            amt = f"{item['amount']:.2f}"
            items += f"{desc:<23}{amt:>7}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories):
    chart = "Percentage spent by category\n"
    
    # Calculate withdrawals for each category
    withdrawals = []
    for cat in categories:
        spent = sum(abs(item["amount"]) for item in cat.ledger if item["amount"] < 0)
        withdrawals.append(spent)
        
    total_spent = sum(withdrawals)
    
    # Calculate percentages rounded down to the nearest 10
    if total_spent == 0:
        percentages = [0 for _ in categories]
    else:
        percentages = [math.floor((w / total_spent) * 100 / 10) * 10 for w in withdrawals]

    # Build the bar chart section from 100 down to 0
    for i in range(100, -1, -10):
        line = f"{i:3}| "
        for p in percentages:
            if p >= i:
                line += "o  "
            else:
                line += "   "
        chart += line + "\n"

    # Horizontal line below the bars
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Category names written vertically below the bar
    max_len = max(len(cat.name) for cat in categories)
    names = [cat.name for cat in categories]
    
    name_lines = []
    for i in range(max_len):
        line = "     "
        for name in names:
            if i < len(name):
                line += name[i] + "  "
            else:
                line += "   "
        name_lines.append(line)
    
    chart += "\n".join(name_lines)
    return chart
