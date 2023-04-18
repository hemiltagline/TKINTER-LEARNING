from tkinter import *
import tkinter as tk

root = Tk()
root.geometry("250x170")

my_var = StringVar()

# defining the callback function (observer)
def my_callback(var, index, mode):
    print("Traced variable {}".format(my_var.get()))


# registering the observer
my_var.trace_add("write", my_callback)

Label(root, textvariable=my_var).grid(row=2, column=0, padx=5, pady=5)

Entry(root, textvariable=my_var).grid(row=2, column=1, padx=5, pady=5)

L1 = Label(root, text="User Name")
L1.grid(row=0, column=0)
L2 = Label(root, text="Password")
L2.grid(row=1, column=0)

mystr = StringVar()
mystr.set("username@xyz.com")

email_label = Label(root, text=mystr.get())
email_label.grid(row=0, column=1, padx=10, pady=10)

passwd = Entry(root)
passwd.grid(row=1, column=1, padx=10, pady=10)


# Create label
l = Label(root, text="Fact of the Day")
l.config(font=("Courier", 14))
l.grid(row=3, column=0, columnspan=2)

Fact = """A man can be arrested in
Italy for wearing a skirt in public."""

# Create button for next text.
b1 = Button(
    root,
    text="Next",
)

# Create an Exit button.
b2 = Button(root, text="Exit", command=root.destroy)

b1.grid(row=4, column=0, padx=5, pady=5)
b2.grid(row=4, column=1, padx=5, pady=5)

# Insert The Fact.
T = Text(root, height=5, width=52)


# root.geometry("300x200")

w = Label(root, text="GeeksForGeeks", font="50")
w.pack()

msg = Message(root, text="A computer science portal for geeks")

msg.pack()


root.mainloop()
