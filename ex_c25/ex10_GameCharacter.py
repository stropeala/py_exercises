# Exercise 10: OOP Exercise
# Create a GameCharacter class.

# Attributes:
# • health (private) starting at 100

# Tasks:
# 1. take_damage(value)
# 2. heal(value)
# 3. Health must stay between 0 and 100.
# 4. get_health()

# Goal: protect logical constraints.
# Abstraction


class GameCharacter:
    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, new_health: int):
        self._health = max(0, min(100, new_health))

    def take_damage(self, value: int) -> None:
        if value <= 0:
            raise ValueError("Damage value must be positive")
        self.health -= value

    def heal(self, value: int) -> None:
        if value <= 0:
            raise ValueError("Heal value must be positive")
        self.health += value

    def is_alive(self):
        return self.health > 0

    def get_health(self):
        return self.health

    def __str__(self):
        status = "Alive" if self.is_alive() else "Dead"
        return f"{self.name} — Health: {self.health}/100 ({status})"


if __name__ == "__main__":
    ionel = GameCharacter("Ionel")
    print(ionel)

    ionel.take_damage(40)
    print(ionel)

    ionel.heal(20)
    print(ionel)

    ionel.heal(999)
    print(ionel)

    ionel.take_damage(999)
    print(ionel)
