from plates.plates import *

def main():
    test_is_valid()
    test_check_lengh()

def test_is_valid():
    assert is_valid("H") == False
    assert is_valid("CS50") == True
    assert is_valid("A2") == False

def test_check_lengh():
    assert check_length("A2") == True
    assert check_length("cs") == True
    assert check_length("2ANIPBIPRB") == False
    assert check_length("CS50") == True


if __name__ == "__main__":
    main()

