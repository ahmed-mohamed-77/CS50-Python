from tkinter import *
from tkinter import messagebox

def main():
    def disable_all_buttons():
        b1.config(state=DISABLED)
        b2.config(state=DISABLED)
        b3.config(state=DISABLED)
        b4.config(state=DISABLED)
        b5.config(state=DISABLED)
        b6.config(state=DISABLED)
        b7.config(state=DISABLED)
        b8.config(state=DISABLED)
        b9.config(state=DISABLED)

    def check_win():
        winner = False
        if (b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X") or \
           (b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X") or \
           (b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X") or \
           (b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X") or \
           (b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X") or \
           (b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X") or \
           (b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X") or \
           (b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X"):
            winner = True
            disable_all_buttons()
            messagebox.showinfo(title="Congratulations!", message="X wins!")
        elif (b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O") or \
             (b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O") or \
             (b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O") or \
             (b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O") or \
             (b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O") or \
             (b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O") or \
             (b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O") or \
             (b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O"):
            winner = True
            disable_all_buttons()
            messagebox.showinfo(title="Congratulations!", message="O wins!")
        elif counter == 8:
            messagebox.showinfo(title="Tie Game", message="It's a tie!")
        return winner

    def b_click(b):
        global clicked, counter
        if b["text"] == " " and clicked:
            b["text"] = "X"
            clicked = False
            counter += 1
            check_win()
        elif b["text"] == " " and not clicked:
            b["text"] = "O"
            clicked = True
            counter += 1
            check_win()
        else:
            messagebox.showinfo(title="Invalid Move", message="That box is already selected!\nPick another box.")

    def reset():
        global b1, b2, b3, b4, b5, b6, b7, b8, b9
        global clicked, counter
        clicked = True
        counter = 0
        # Build our Buttons
        b1 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="gray25", fg="white", command=lambda: b_click(b1))
        b2 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="gray25", fg="white", command=lambda: b_click(b2))
        b3 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="gray25", fg="white", command=lambda: b_click(b3))
        b4 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="gray25", fg="white", command=lambda: b_click(b4))
        b5 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="gray25", fg="white", command=lambda: b_click(b5))
        b6 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="gray25", fg="white", command=lambda: b_click(b6))
        b7 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="gray25", fg="white", command=lambda: b_click(b7))
        b8 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="gray25", fg="white", command=lambda: b_click(b8))
        b9 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="gray25", fg="white", command=lambda: b_click(b9))

        # Grid Our Buttons
        b1.grid(row=0, column=0)
        b2.grid(row=0, column=1)
        b3.grid(row=0, column=2)
        b4.grid(row=1, column=0)
        b5.grid(row=1, column=1)
        b6.grid(row=1, column=2)
        b7.grid(row=2, column=0)
        b8.grid(row=2, column=1)
        b9.grid(row=2, column=2)

    global root, clicked, counter
    root = Tk()
    root.title("Welcome to Tic Tac Toe")
    clicked = True
    counter = 0

    reset()

    # Create Menu
    my_menu = Menu(root)
    root.config(menu=my_menu)

    # Create option menu
    option_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="Options", menu=option_menu)
    option_menu.add_command(label="Reset Game", command=reset)

    root.mainloop()


if __name__ == "__main__":
    main()
