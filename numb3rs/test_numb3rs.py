from numb3rs import validate

def test_validate():
    # Valid IP addresses
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True
    assert validate("192.168.1.1") == True

    # Invalid IP addresses
    assert validate("512.512.512.512") == False  # Beyond valid range
    assert validate("1.2.3.1000") == False  # Beyond valid range
    assert validate("10.10.10.10.10") == False  # Too many segments
    assert validate("256.0.0.1") == False  # Beyond valid range
    assert validate("2567.2567.0.1") == False
    assert validate("256.0.2567.1") == False
    assert validate("26.512.512.512") == False
  


def test_false_ip():
    # Invalid inputs
    assert validate("cat") == False  # Non-numeric characters
    assert validate("256.256.256.256") == False  # Beyond valid range

    # Edge cases
    assert validate("") == False  # Empty input
    assert validate("192.168.0.1/24") == False  # IP with subnet notation


