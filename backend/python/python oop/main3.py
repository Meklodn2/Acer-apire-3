class BankAccount:
    def __init__(self, initial_balance):
       
        self._balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Insufficient balance or invalid amount")

    def get_balance(self):
        return self._balance
account1 = BankAccount(1000)
account2 = BankAccount(500)


account1.deposit(200)
account2.deposit(100)

account1.withdraw(150)
account2.withdraw(50)


print(f"Account 1 balance: {account1.get_balance()}")
print(f"Account 2 balance: {account2.get_balance()}")
