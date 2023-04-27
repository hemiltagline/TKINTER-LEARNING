# from tkinter import *


# # Create the root window
# root = Tk()
# root.title("Root Window")
# root.geometry("450x300")

# # Create label for root window
# label1 = Label(root, text="This is the main window")

# # define a function for 2nd toplevel
# # window which is not associated with
# # any parent window
# def open_Toplevel2():

#     # Create widget
#     top2 = Toplevel()

#     # define title for window
#     top2.title("Toplevel2")

#     # specify size
#     top2.geometry("200x100")

#     # Create label
#     label = Label(top2, text="This is a Toplevel2 window")

#     # Create exit button.
#     button = Button(top2, text="Exit", command=top2.destroy)

#     label.pack()
#     button.pack()

#     # Display until closed manually.
#     top2.mainloop()


# # define a function for 1st toplevel
# # which is associated with root window.
# def open_Toplevel1():

#     # Create widget
#     top1 = Toplevel(root)

#     # Define title for window
#     top1.title("Toplevel1")

#     # specify size
#     top1.geometry("200x200")

#     # Create label
#     label = Label(top1, text="This is a Toplevel1 window")

#     # Create Exit button
#     button1 = Button(top1, text="Exit", command=top1.destroy)

#     # create button to open toplevel2
#     button2 = Button(top1, text="open toplevel2", command=open_Toplevel2)

#     label.pack()
#     button2.pack()
#     button1.pack()

#     # Display until closed manually
#     top1.mainloop()


# # Create button to open toplevel1
# button = Button(root, text="open toplevel1", command=open_Toplevel1)
# label1.pack()

# # position the button
# button.place(x=155, y=50)

# # Display until closed manually
# root.mainloop()


import tkinter as tk
import tkinter.messagebox as messagebox
import time


class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.master.resizable(False, False)
        self.turn = "X"
        self.board = [["", "", ""] for _ in range(3)]
        self.buttons = []
        self.create_board()

    def create_board(self):
        for row in range(3):
            button_row = []
            for col in range(3):
                button = tk.Button(
                    self.master,
                    text="",
                    font=("Arial", 40),
                    width=3,
                    height=1,
                    command=lambda row=row, col=col: self.click_button(row, col),
                )
                button.grid(row=row, column=col, padx=5, pady=5)
                button_row.append(button)
            self.buttons.append(button_row)

    def click_button(self, row, col):
        if self.board[row][col] == "":
            self.buttons[row][col].config(text=self.turn, fg="white", bg="green")
            self.buttons[row][col].update_idletasks()
            time.sleep(0.5)
            self.buttons[row][col].config(bg="SystemButtonFace")
            self.board[row][col] = self.turn
            self.check_win()
            self.turn = "O" if self.turn == "X" else "X"

    def check_win(self):
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != "":
                self.declare_winner(self.board[row][0])
                return
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != "":
                self.declare_winner(self.board[0][col])
                return
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            self.declare_winner(self.board[0][0])
            return
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            self.declare_winner(self.board[0][2])
            return

    def declare_winner(self, player):
        messagebox.showinfo("Winner!", f"{player} wins!")
        self.reset_board()

    def reset_board(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text="", state="normal")
                self.board[row][col] = ""
        self.turn = "X"


root = tk.Tk()
game = TicTacToe(root)
root.mainloop()
