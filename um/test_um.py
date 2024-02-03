from um.um import count
import pytest


def test_require_spaces_around_um():
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2
    assert count("umm") == 0  # No spaces around "um"
    assert count("hello, um, world") == 1  # Spaces around "um"
    assert count("hello,um,world") == 1  # No spaces around "um"
    assert count("hello, um?") == 1  # Spaces around "um"
    assert count("umm") == 0


# Test case 2: Modify count function to mistakenly count "um" in words
def test_mistakenly_count_in_words():
    with pytest.raises(AssertionError):
        assert count("yummy") == 1


# Test case 3: Correct the mistake and introduce a new mistake by requiring spaces
def test_require_um():
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2
    with pytest.raises(AssertionError):
        assert count("umm") == 1
        assert count("hello,um,world") == 1
