# 5) Bank Account Basics
# Create a class BankAccount with:
# - attributes: owner, balance=0.0
# - methods: deposit(amount), withdraw(amount)
# - Do not allow negative deposits or withdrawals
# - Do not allow balance to go below 0


class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self._owner = owner
        self._balance = balance

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, new_owner: str):
        self._owner = new_owner

    @property
    def balance(self):
        return f"\nBalance: {self._balance} RON\n"

    @balance.setter
    def balance(self, new_balance: float):
        if new_balance < 0:
            raise ValueError("Value below zero!")
        self._balance = new_balance

    def deposit(self, amount: float):
        if amount < 0:
            raise ValueError("Deposit error: Negative amount!")

        self.balance = self._balance + amount
        return f"\nAmount Deposited: {amount} RON\nNew Balance: {self._balance} RON\n"

    def withdraw(self, amount: float):
        if amount < 0:
            raise ValueError("Withdrawal error: Negative amount!")
        if self._balance < amount:
            raise ValueError("Withdrawal error: Insufficient funds!")

        self.balance = self._balance - amount
        return f"\nAmount Withdrawn: {amount} RON\nNew Balance: {self._balance} RON\n"


if __name__ == "__main__":
    person1 = BankAccount("Ion", 125)
    print(person1.balance)
    print(person1.deposit(10))
    print(person1.deposit(-10))
    print(person1.withdraw(10))
    print(person1.withdraw(-10))
    print(person1.withdraw(-125))
