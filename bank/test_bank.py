from bank import value


def test_hello():
    assert value("Hello") == 0
    assert value("Hello, ahmed") == 0


def test_start_with_h():
    assert value("hey") == 20
    assert value("How's it going") == 20
    assert value("How you doing") == 20


# not starting with the letter(h) or hello
def test_start_with_any_other_word():
    assert value("What's up") == 100
    assert value("Morning! ...") == 100
    assert value("It's good to see you") == 100
