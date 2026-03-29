# Exercise 4: OOP Exercise
# Improve the BankAccount class.

# Withdrawals should not be allowed if the balance becomes negative.
# Tasks:
# 1. Modify withdraw().
# 2. If withdrawal is larger than balance, raise an error.

# Goal: enforce rules inside a class.


class BankAccount:
    def __init__(self, owner: str, balance: float) -> None:
        self.owner = owner
        self.balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, new_balance: float) -> None:
        if new_balance < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = new_balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Cannot deposit/withdraw zero or negative amount")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Cannot deposit/withdraw zero or negative amount")
        if amount > self.balance:
            raise ValueError("Balance too low")
        self.balance -= amount


if __name__ == "__main__":
    ionel = BankAccount("Ionel", 2500)
    print(ionel.balance)

    ionel.balance = 3500
    print(ionel.balance)

    try:
        ionel.balance = -5
    except ValueError as error:
        print(f"Error: {error}")

    ionel.deposit(1000)
    print(ionel.balance)

    ionel.withdraw(3500)
    print(ionel.balance)

    try:
        ionel.withdraw(2000)
    except ValueError as error:
        print(f"Error: {error}")
