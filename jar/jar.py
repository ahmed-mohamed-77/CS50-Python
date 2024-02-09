# Define the Jar class
class Jar:
    def __init__(self, capacity=12):
        self._cookies = 0
        self.capacity = capacity

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer.")
        self._capacity = capacity

    @property
    def size(self) -> int:
        return self._cookies

    def __str__(self) -> str:
        return "🍪" * self._cookies

    def deposit(self, n) -> None:
        if not isinstance(n, int) or n < 0:
            raise ValueError("Number of cookies must be a non-negative integer.")
        if self._cookies + n > self._capacity:
            raise ValueError("Adding cookies would exceed the jar's capacity.")
        self._cookies += n

    def withdraw(self, n) -> None:
        if not isinstance(n, int) or n < 0:
            raise ValueError("Number of cookies must be a non-negative integer.")
        if self._cookies - n < 0:
            raise ValueError("Not enough cookies in the jar to withdraw.")
        self._cookies -= n



