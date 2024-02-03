from um import count
import pytest


def test_require_spaces_around_um():
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2
    assert count("umm") == 0
    assert count("hello, um, world") == 1
    assert count("hello,um,world") == 1
    assert count("hello, um?") == 1
    assert count("umm") == 0



def test_mistakenly_count_in_words():
    with pytest.raises(AssertionError):
        assert count("yummy") == 1


def test_require_um():
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2
    with pytest.raises(AssertionError):
        assert count("umm") == 1
        assert count("hello,um,world") == 1
