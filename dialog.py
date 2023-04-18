from tkinter import *
from tkinter import messagebox

# create instance of TK()
main = Tk()


main.title("example")
main.iconbitmap(r"images/google-logo.png")


# function to use the askquestion() function
def Submit():
    messagebox.askquestion("Form", "Do you want to Submit")


# create Window and set size
main.geometry("300x300")

# create Submit button and place in grid
B1 = Button(main, text="Submit", command=Submit)
B1.grid(row=0, column=0, padx=10, pady=10)

# function to check name
def check():
    messagebox.showerror("Error", "Your name is incorrect.")


# create Check button and place in grid
B2 = Button(main, text="Check", command=check)
B2.grid(row=1, column=0, padx=10, pady=10)

# run the main loop


# Python program to create
# yes/no message box

from tkinter import messagebox as mb


def call():
    res = mb.askquestion("Exit Application", "Do you really want to exit")

    if res == "yes":
        root.destroy()

    else:
        mb.showinfo("Return", "Returning to main application")


# Driver's code
root = Tk()
canvas = Canvas(root, width=200, height=200)

canvas.pack()
b = Button(root, text="Quit Application", command=call)

canvas.create_window(100, 100, window=b)


from tkinter.messagebox import *

# Showing various messages

print(askokcancel("askokcancel", "Ok or Cancel"))

print(askquestion("askquestion", "Question?"))

print(askretrycancel("askretrycancel", "Retry or Cancel"))

print(askyesno("askyesno", "Yes or No"))

print(askyesnocancel("askyesnocancel", "Yes or No or Cancel"))

print(showerror("showerror", "Error"))

print(showinfo("showinfo", "Information"))

print(showwarning("showwarning", "Warning"))

# print statement is used so that we can
# print the returned value by the function


mainloop()
