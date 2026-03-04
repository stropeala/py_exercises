# 10) Inventory Item
# Create Item with:
# - attributes: name, stock
# - methods: add_stock(), remove_stock()
# - prevent negative stock


class Item:
    def __init__(self, name: str, stock: int) -> None:
        self._name = name
        self._stock = stock

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        self._name = new_name

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, new_stock: int) -> None:
        if new_stock < 0:
            raise ValueError("Stock cannot be negative!")
        self._stock = new_stock

    def add_stock(self, amount: int):
        if amount < 0:
            raise ValueError("Amount cannot be negative!")

        self.stock = self._stock + amount
        return f"\nAmount added: {amount}\nNew Stock = {self._stock}\n"

    def remove_stock(self, amount: int):
        if amount < 0:
            raise ValueError("Amount cannot be negative!")

        if amount > self._stock:
            raise ValueError("Insufficient stock!")

        self.stock = self._stock - amount
        return f"\nAmount removed: {amount}\nNew Stock = {self._stock}\n"


if __name__ == "__main__":
    item1 = Item("Matura", 20)
    print(item1.stock)
    print(item1.add_stock(5))
    # print(item1.add_stock(-5))
    print(item1.remove_stock(5))
    # print(item1.remove_stock(-5))
    print(item1.remove_stock(21))
