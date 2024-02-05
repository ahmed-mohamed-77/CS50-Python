from numb3rs import validate

def test_validate():
    # Valid IP addresses
    assert validate("127.0.0.1") is True
    assert validate("255.255.255.255") is True
    assert validate("0.0.0.0") is True
    assert validate("192.168.1.1") is True

    # Invalid IP addresses
    assert validate("512.512.512.512") is False  # Beyond valid range
    assert validate("1.2.3.1000") is False  # Beyond valid range
    assert validate("10.10.10.10.10") is False  # Too many segments
    assert validate("256.0.0.1") is False  # Beyond valid range
    assert validate("2567.2567.0.1") is False
    assert validate("256.0.2567.1") is False
    assert validate("256.0.0.2567") is False


def test_false_ip():
    # Invalid inputs
    assert validate("cat") is False  # Non-numeric characters
    assert validate("256.256.256.256") is False  # Beyond valid range

    # Edge cases
    assert validate("") is False  # Empty input
    assert validate("192.168.0.1/24") is False  # IP with subnet notation


