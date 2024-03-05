from tic_tac_toe.project import main  # Assuming main is a module or class
main = main()
def test_check_win_horizontal_X():
    """Tests if check_win correctly identifies a horizontal win for X."""
    main.buttons = ["X", "X", "X", " ", " ", " ", " ", " ", " "]  # Set button states
    assert main.check_win() is True  # Assert that X wins

def test_check_win_vertical_O():
    """Tests if check_win correctly identifies a vertical win for O."""
    main.buttons = [" ", " ", "O", " ", "O", "O", " ", " ", "O"]  # Set button states
    assert main.check_win() is True  # Assert that O wins
