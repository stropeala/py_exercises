# 18) Shopping Cart
# Create Cart with:
# - attribute: prices (list)
# - methods: add(price), total()


class Cart:
    def __init__(self, prices: list) -> None:
        self._prices = prices

    @property
    def prices(self):
        return self._prices

    @prices.setter
    def prices(self, new_prices: list):
        if new_prices == "":
            raise ValueError("List cannor be empty")

        for i in new_prices:
            if i <= 0:
                raise ValueError("Price cannot be negative or zero!")

        self._prices = new_prices

    def add(self, price: int):
        if price <= 0:
            raise ValueError("Price cannot be negative or zero!")

        self.prices.append(price)

    def total(self):
        return sum(self.prices)


if __name__ == "__main__":
    cart1 = Cart([1, 2, 34, 5])
    print(cart1.prices)
    cart1.add(67)
    print(cart1.prices)
    print(cart1.total())
