# 16) Timer
# Create Timer with:
# - attribute: seconds
# - methods: tick(), is_finished()
import time


class Timer:
    def __init__(self, seconds: int) -> None:
        self._seconds = seconds

    @property
    def seconds(self):
        return self._seconds

    @seconds.setter
    def seconds(self, new_seconds: int):
        if new_seconds < 0:
            raise ValueError("Seconds cannot be 0!")

        self._seconds = new_seconds

    def tick(self):
        t = self.seconds
        while t:
            time.sleep(1)
            t -= 1
            print("Tick!")
        return "Finished!"


if __name__ == "__main__":
    timer = Timer(10)
    print(timer.tick())
