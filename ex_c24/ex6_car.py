# 6) Class Attribute: Counting Instances
# Create a class Car with:
# - class attribute: total_cars
# - increment it every time a new instance is created


class Car:
    instances = 0

    def __init__(self, total_cars: list) -> None:
        self._total_cars = total_cars
        Car.instances += 1

    @property
    def total_cars(self):
        return self._total_cars

    @total_cars.setter
    def total_cars(self, new_total_cars: list):
        self._total_cars = new_total_cars


if __name__ == "__main__":
    bmw = Car(["520d", "740i"])
    mercedes = Car(["A220", "C45", "SLK"])
    audi = Car(["A7", "A8", "A5"])
    print(Car.instances)
