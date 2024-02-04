from bank import value


def test_hello():
    assert value("hello") == 0
    assert value("hello, ahmed") == 0


def test_start_with_h():
    assert value("hey") == 20
    assert value("how's it going") == 20
    assert value("how you doing") == 20


# not starting with the letter(h) or hello
def test_start_with_any_other_word():
    assert value("what's up") == 100
    assert value("morning! ...") == 100
    assert value("it's good to see you") == 100
