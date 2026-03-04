# 13) Dice
# Create Dice with:
# - attribute: sides
# - method: roll() returns random number between 1 and sides


import random


class Dice:
    def __init__(self, sides: int) -> None:
        self._sides = sides

    @property
    def sides(self):
        return self._sides

    @sides.setter
    def sides(self, new_sides: int):
        if new_sides <= 0:
            raise ValueError("Zero!")
        self._sides = new_sides

    def roll(self):
        rolled = random.randint(1, self.sides)
        return rolled


if __name__ == "__main__":
    dice1 = Dice(6)
    print(dice1.roll())
