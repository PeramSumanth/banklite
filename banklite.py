import json
import os
from datetime import datetime


class Account:
    def __init__(self, acc_id, name, balance=0.0):
        self.id = acc_id
        self.name = name
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit must be greater than 0")
            return False
        self.balance += amount
        log = f"{datetime.now()} - Deposited: {amount}, Balance: {self.balance}"
        self.transactions.append(log)
        print("Deposit successful")
        return True

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal must be greater than 0")
            return False
        if amount > self.balance:
            print("Insufficient funds")
            return False
        self.balance -= amount
        log = f"{datetime.now()} - Withdrew: {amount}, Balance: {self.balance}"
        self.transactions.append(log)
        print("Withdrawal successful")
        return True

    def get_balance(self):
        return self.balance

    def get_history(self):
        return self.transactions

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "balance": self.balance,
            "transactions": self.transactions
        }

    @classmethod
    def from_dict(cls, data):
        acc = cls(data["id"], data["name"], data["balance"])
        acc.transactions = data["transactions"]
        return acc


class Bank:
    def __init__(self):
        self.accounts = []

    def create_account(self, name, start_balance=0.0):
        acc_id = len(self.accounts) + 1
        acc = Account(acc_id, name, start_balance)
        self.accounts.append(acc)
        print(f"Account created. ID: {acc_id}, Name: {name}")
        return acc

    def find_account_by_id(self, acc_id):
        for acc in self.accounts:
            if acc.id == acc_id:
                return acc
        return None

    def deposit_to_account(self, acc_id, amount):
        acc = self.find_account_by_id(acc_id)
        if acc:
            acc.deposit(amount)
        else:
            print("Account not found")

    def withdraw_from_account(self, acc_id, amount):
        acc = self.find_account_by_id(acc_id)
        if acc:
            acc.withdraw(amount)
        else:
            print("Account not found")

    def show_account_details(self, acc_id):
        acc = self.find_account_by_id(acc_id)
        if acc:
            print(f"--- Account ID: {acc.id} ---")
            print(f"Name: {acc.name}")
            print(f"Balance: {acc.balance}")
            print("Transaction History:")
            for t in acc.get_history():
                print("   ", t)
        else:
            print("Account not found")

    def save_to_file(self, filename="bank.json"):
        data = [acc.to_dict() for acc in self.accounts]
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print("Data saved successfully")

    def load_from_file(self, filename="bank.json"):
        if os.path.exists(filename):
            with open(filename, "r") as f:
                data = json.load(f)
                self.accounts = [Account.from_dict(d) for d in data]
            print("Data loaded successfully")
        else:
            print("No existing data found")


# ========== Console App ==========
def main():
    bank = Bank()
    bank.load_from_file()

    while True:
        print("\n===== BankLite Menu =====")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. View Account Details")
        print("5. Save & Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter account holder name: ")
            bal = float(input("Enter starting balance: "))
            bank.create_account(name, bal)

        elif choice == "2":
            acc_id = int(input("Enter account ID: "))
            amt = float(input("Enter deposit amount: "))
            bank.deposit_to_account(acc_id, amt)

        elif choice == "3":
            acc_id = int(input("Enter account ID: "))
            amt = float(input("Enter withdrawal amount: "))
            bank.withdraw_from_account(acc_id, amt)

        elif choice == "4":
            acc_id = int(input("Enter account ID: "))
            bank.show_account_details(acc_id)

        elif choice == "5":
            bank.save_to_file()
            print("Exiting. Goodbye!")
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
