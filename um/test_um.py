from um.um import count


def test_upper_lower_case():
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2


def test_word_with_um():
    assert count("yummy") == 0
    assert count("umm") == 0


def test_surrounded_by_space():
    assert count("hello, um, world") == 1
    assert count("hello, um?") == 1

