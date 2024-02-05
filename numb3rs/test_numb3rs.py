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

def test_false_ip():
    # Invalid inputs
    assert validate("cat") is False  # Non-numeric characters
    assert validate("256.256.256.256") is False  # Beyond valid range

    # Edge cases
    assert validate("") is False  # Empty input
    assert validate("192.168.0.1/24") is False  # IP with subnet notation

def test_invalid_subnet():
    # Testing an additional function for handling subnet notation
    assert validate_subnet("192.168.0.1/24") is False

def test_valid_subnet():
    # Testing an additional function for handling subnet notation
    assert validate_subnet("192.168.0.1/24") is False
    assert validate_subnet("192.168.0.1/32") is True

def test_ipv6_support():
    # Testing if the function supports IPv6 validation
    assert validate_ipv6("2001:0db8:85a3:0000:0000:8a2e:0370:7334") is True
    assert validate_ipv6("127.0.0.1") is False  # Should return False for IPv4

def test_ip_with_port():
    # Testing if the function correctly rejects IP addresses with ports
    assert validate_ip_with_port("192.168.0.1:8080") is False
    assert validate_ip_with_port("127.0.0.1") is True
