from plates.plates import *


def test_is_valid():
    assert is_valid("CS50") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False


def test_check_lengh():
    assert is_valid("A2") == False
    assert is_valid("AA") == True
    assert is_valid("2A") == False
    assert is_valid("22") == False

def min_max_character():
    assert is_valid("ABCDEFGH") == False
    assert is_valid("H") == False
    assert is_valid("A") == False

def test_num_zero():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False

def test_punctuation():
    assert is_valid("PT3.14") == False
    assert is_valid("PT!314") == False
    assert is_valid("PT 314") == False



