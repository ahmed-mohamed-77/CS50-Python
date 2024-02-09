class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError
        self._capacity = capacity

    @property
    def size(self) -> int:
        return self._cookies

    def __str__(self) -> str:
        return "🍪" * self._cookies

    def deposit(self, n) -> None:
        if not isinstance(n, int) or n < 0:
            raise ValueError
        if self._cookies + n > self._capacity:
            raise ValueError
        self._cookies += n

    def withdraw(self, n) -> None:
        if not isinstance(n, int) or n < 0:
            raise ValueError
        if self._cookies - n < 0:
            raise ValueError
        self._cookies -= n
