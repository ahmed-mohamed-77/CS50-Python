from jar import Jar
import pytest


class TestJar:
    @pytest.fixture
    def jar(self):
        return Jar(10)

    @pytest.mark.parametrize("num_cookies", [5, 7, 10])
    def test_deposit(self, jar, num_cookies):
        jar.deposit(num_cookies)
        assert jar.size == num_cookies

    @pytest.mark.parametrize("num_cookies", [3, 5, 8])
    def test_withdraw(self, jar, num_cookies):
        jar.deposit(10)
        jar.withdraw(num_cookies)
        assert jar.size == (10 - num_cookies)

    def test_deposit_overflow(self, jar):
        jar.deposit(8)
        with pytest.raises(ValueError):
            jar.deposit(5)

    def test_withdraw_underflow(self, jar):
        jar.deposit(5)
        with pytest.raises(ValueError):
            jar.withdraw(8)
