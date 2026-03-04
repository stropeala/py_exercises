# 9) Instance Tax Override
# Create BookFlexibleTax:
# - use self.tax_rate inside price_with_tax()
# - allow overriding tax per instance


class Book:
    tax_rate = 0.05

    def __init__(self, title: str, price: float) -> None:
        self._title = title
        self._price = price

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title: str):
        if new_title == "":
            raise ValueError("Value is empty!")
        self._title = new_title

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price: float):
        if new_price < 0:
            raise ValueError("Value below zero!")
        self._price = new_price

    def price_with_tax(self):
        return self.price + Book.tax_rate * self.price


class BookFlexibleTax(Book):
    tax_rate = 0.15

    def price_with_tax(self):
        return self.price + self.tax_rate * self.price


if __name__ == "__main__":
    book1 = Book("Toate panzele sus", 10)
    print(book1.price_with_tax())

    book2 = BookFlexibleTax("Ion", 20)
    print(book2.price_with_tax())

    book3 = BookFlexibleTax("Moby Dick", 20)
    book3.tax_rate = 0.10
    print(book3.price_with_tax())
