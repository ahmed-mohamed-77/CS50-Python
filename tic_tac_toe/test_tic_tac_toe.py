from tkinter import *
from tkinter import messagebox
from tic_tac_toe.project import main


def test_check_win():
    # Create a mock tkinter root window
    root = Tk()

    # Mock buttons
    b1 = Button(root, text="X")
    b2 = Button(root, text="X")
    b3 = Button(root, text="X")
    b4 = Button(root, text="O")
    b5 = Button(root, text="O")
    b6 = Button(root, text=" ")
    b7 = Button(root, text=" ")
    b8 = Button(root, text=" ")
    b9 = Button(root, text=" ")

    # Set up a sample scenario for X winning
    b1["text"] = "X"
    b2["text"] = "X"
    b3["text"] = "X"
    assert main.check_win(b1, b2, b3, b4, b5, b6, b7, b8, b9) == True

    # Set up a sample scenario for O winning
    b4["text"] = "O"
    b5["text"] = "O"
    b6["text"] = "O"
    assert main.check_win(b1, b2, b3, b4, b5, b6, b7, b8, b9) == True

    # Set up a sample scenario for a draw
    b7["text"] = "X"
    b8["text"] = "O"
    b9["text"] = "X"
    assert main.check_win(b1, b2, b3, b4, b5, b6, b7, b8, b9) == False


def test_reset():
    # Create a mock tkinter root window
    root = Tk()

    # Mock buttons
    b1 = Button(root, text="X")
    b2 = Button(root, text="O")
    b3 = Button(root, text=" ")
    b4 = Button(root, text=" ")
    b5 = Button(root, text="O")
    b6 = Button(root, text="X")
    b7 = Button(root, text="O")
    b8 = Button(root, text="X")
    b9 = Button(root, text=" ")

    # Set up a scenario where buttons have different text
    assert b1["text"] == "X"
    assert b2["text"] == "O"
    assert b3["text"] == " "
    assert b4["text"] == " "
    assert b5["text"] == "O"
    assert b6["text"] == "X"
    assert b7["text"] == "O"
    assert b8["text"] == "X"
    assert b9["text"] == " "

    # Reset the board
    main.reset(b1, b2, b3, b4, b5, b6, b7, b8, b9)

    # Check if all buttons are reset to " "
    assert b1["text"] == " "
    assert b2["text"] == " "
    assert b3["text"] == " "
    assert b4["text"] == " "
    assert b5["text"] == " "
    assert b6["text"] == " "
    assert b7["text"] == " "
    assert b8["text"] == " "
    assert b9["text"] == " "


def test_b_click():
    # Create a mock tkinter root window
    root = Tk()

    # Mock buttons
    b1 = Button(root, text=" ")
    b2 = Button(root, text="X")
    b3 = Button(root, text="O")
    b4 = Button(root, text=" ")
    b5 = Button(root, text="X")
    b6 = Button(root, text="O")
    b7 = Button(root, text="X")
    b8 = Button(root, text=" ")
    b9 = Button(root, text="O")

    # Mock counter and clicked status
    clicked = True
    counter = 1

    # Simulate clicking on a button with " "
    main.b_click(b1, clicked, counter)
    assert b1["text"] == "X"
    assert clicked == False
    assert counter == 2

    # Simulate clicking on a button with "X"
    main.b_click(b2, clicked, counter)
    assert b2["text"] == "X"
    assert clicked == False
    assert counter == 3

    # Simulate clicking on a button with "O"
    main.b_click(b3, clicked, counter)
    assert b3["text"] == "O"
    assert clicked == True
    assert counter == 4

    # Simulate clicking on a button with "X"
    main.b_click(b4, clicked, counter)
    assert b4["text"] == "X"
    assert clicked == True
    assert counter == 5

    # Simulate clicking on a button with "X"
    main.b_click(b5, clicked, counter)
    assert b5["text"] == "X"
    assert clicked == True
    assert counter == 6

    # Simulate clicking on a button with "O"
    main.b_click(b6, clicked, counter)
    assert b6["text"] == "O"
    assert clicked == False
    assert counter == 7

    # Simulate clicking on a button with "X"
    main.b_click(b7, clicked, counter)
    assert b7["text"] == "X"
    assert clicked == False
    assert counter == 8

    # Simulate clicking on a button with " "
    main.b_click(b8, clicked, counter)
    assert b8["text"] == "O"
    assert clicked == True
    assert counter == 9

    # Simulate clicking on a button with "O"
    main.b_click(b9, clicked, counter)
    assert b9["text"] == "O"
    assert clicked == True
    assert counter == 10

    # Check if clicking on a disabled button does not change its text
    main.disable_all_buttons(b1, b2, b3, b4, b5, b6, b7, b8, b9)
    main.b_click(b1, clicked, counter)
    assert b1["text"] == "O"


if __name__ == "__main__":
    main()
