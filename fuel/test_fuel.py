from 
import pytest

# zero division
def test_zero_division():
  with pytest.raises(ZeroDivisionError):
    assert convert("1/0")

# value error
def test_value():
  with pytest.raises(ValueError):
    assert convert("cat/dog")

def test_convert():
  assert convert("0/1") == 0
  assert convert("3/4") == 75
  assert convert("4/4") == 1

def test_gauge():
  assert gauge(99) == "F"
  assert gauge(0) == "E"
  assert gauge("3/4") == "75%"
