from tic_tac_toe.project import main
import pytest
from tkinter import Button
from tkinter import Tk
from tkinter import Menu
from tkinter import messagebox



def test_check_win_X_wins():
    root = Tk()
    main.root = root  # Set the main function's root for testing

    # Mock the buttons with X winning scenario
    main.b1 = Button(root, text="X")
    main.b2 = Button(root, text="X")
    main.b3 = Button(root, text="X")
    main.b4 = Button(root, text="O")
    main.b5 = Button(root, text="O")
    main.b6 = Button(root, text=" ")
    main.b7 = Button(root, text=" ")
    main.b8 = Button(root, text=" ")
    main.b9 = Button(root, text=" ")

    assert main.check_win() is True

def test_check_win_O_wins():
    root = Tk()
    main.root = root  # Set the main function's root for testing

    # Mock the buttons with O winning scenario
    main.b1 = Button(root, text="O")
    main.b2 = Button(root, text="O")
    main.b3 = Button(root, text="O")
    main.b4 = Button(root, text="X")
    main.b5 = Button(root, text="X")
    main.b6 = Button(root, text=" ")
    main.b7 = Button(root, text=" ")
    main.b8 = Button(root, text=" ")
    main.b9 = Button(root, text=" ")

    assert main.check_win() is True

def test_check_win_tie_game():
    root = Tk()
    main.root = root  # Set the main function's root for testing

    # Mock the buttons with a tie scenario
    main.b1 = Button(root, text="X")
    main.b2 = Button(root, text="O")
    main.b3 = Button(root, text="X")
    main.b4 = Button(root, text="O")
    main.b5 = Button(root, text="O")
    main.b6 = Button(root, text="X")
    main.b7 = Button(root, text="O")
    main.b8 = Button(root, text="X")
    main.b9 = Button(root, text="X")

    assert main.check_win() is False  # No winner, should return False

def test_b_click():
    root = Tk()
    main.root = root  # Set the main function's root for testing

    # Mock the buttons
    main.b1 = Button(root, text=" ")
    main.b2 = Button(root, text="X")
    main.b3 = Button(root, text="O")
    main.b4 = Button(root, text=" ")
    main.b5 = Button(root, text="X")
    main.b6 = Button(root, text="O")
    main.b7 = Button(root, text="X")
    main.b8 = Button(root, text=" ")
    main.b9 = Button(root, text="O")

    # Mock clicked and counter
    main.clicked = True
    main.counter = 1

    # Simulate clicking on a button with " "
    main.b_click(main.b1)

    assert main.b1["text"] == "X"  # The button should change to X
    assert main.clicked is False  # Clicked should change to False
    assert main.counter == 2  # Counter should increment by 1

    # Simulate clicking on a button with "X"
    main.b_click(main.b2)

    assert main.b2["text"] == "X"  # The button should stay as X
    assert main.clicked is False  # Clicked should remain False
    assert main.counter == 2  # Counter should not change

    # Simulate clicking on a button with "O"
    main.b_click(main.b3)

    assert main.b3["text"] == "O"  # The button should change to O
    assert main.clicked is True  # Clicked should change back to True
    assert main.counter == 3  # Counter should increment by 1

def test_reset():
    root = Tk()
    main.root = root  # Set the main function's root for testing

    # Mock the buttons with different texts
    main.b1 = Button(root, text="X")
    main.b2 = Button(root, text="O")
    main.b3 = Button(root, text=" ")
    main.b4 = Button(root, text=" ")
    main.b5 = Button(root, text="O")
    main.b6 = Button(root, text="X")
    main.b7 = Button(root, text="O")
    main.b8 = Button(root, text="X")
    main.b9 = Button(root, text=" ")

    # Call reset
    main.reset()

    # Check if buttons are reset to " "
    assert main.b1["text"] == " "
    assert main.b2["text"] == " "
    assert main.b3["text"] == " "
    assert main.b4["text"] == " "
    assert main.b5["text"] == " "
    assert main.b6["text"] == " "
    assert main.b7["text"] == " "
    assert main.b8["text"] == " "
    assert main.b9["text"] == " "

    # Check if clicked and counter are reset
    assert main.clicked is True
    assert main.counter == 0

if __name__ == "__main__":
    pytest.main()
