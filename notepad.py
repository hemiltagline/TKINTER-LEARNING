# # importing only those functions
# # which are needed
# from tkinter import *
# from tkinter.ttk import *
# from time import strftime

# # creating tkinter window
# root = Tk()
# root.title("Menu Demonstration")

# # Creating Menubar
# menubar = Menu(root)

# # Adding File Menu and commands
# file = Menu(menubar, tearoff=0)
# menubar.add_cascade(label="File", menu=file)
# file.add_command(label="New File", command=None)
# file.add_command(label="Open...", command=None)
# file.add_command(label="Save", command=None)
# file.add_separator()
# file.add_command(label="Exit", command=root.destroy)

# # Adding Edit Menu and commands
# edit = Menu(menubar, tearoff=0)
# menubar.add_cascade(label="Edit", menu=edit)
# edit.add_command(label="Cut", command=None)
# edit.add_command(label="Copy", command=None)
# edit.add_command(label="Paste", command=None)
# edit.add_command(label="Select All", command=None)
# edit.add_separator()
# edit.add_command(label="Find...", command=None)
# edit.add_command(label="Find again", command=None)

# # Adding Help Menu
# help_ = Menu(menubar, tearoff=0)
# menubar.add_cascade(label="Help", menu=help_)
# help_.add_command(label="Tk Help", command=None)
# help_.add_command(label="Demo", command=None)
# help_.add_separator()
# help_.add_command(label="About Tk", command=None)

# # display Menu
# root.config(menu=menubar)
# mainloop()

from tkinter import *

root = Tk()
root.title("Company Information")
root.geometry("300x200")

w = Label(root, text="Company Names", font="50")
w.pack(pady=50)

menubutton = Menubutton(root, text="LIst of Names")

menubutton.menu = Menu(menubutton)
menubutton["menu"] = menubutton.menu

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()

menubutton.menu.add_checkbutton(label="Tagline Infotech LLP", variable=var1)
menubutton.menu.add_checkbutton(label="Toshal Infotech", variable=var2)
menubutton.menu.add_checkbutton(label="Key Press Infotech", variable=var3)

menubutton.pack()


from tkinter import *
from tkinter.ttk import *

# Progress bar widget
progress = Progressbar(root, orient=HORIZONTAL, length=100, mode="determinate")

# Function responsible for the updation
# of the progress bar value
def bar():
    import time

    progress["value"] = 20
    root.update_idletasks()
    time.sleep(1)

    progress["value"] = 40
    root.update_idletasks()
    time.sleep(1)

    progress["value"] = 50
    root.update_idletasks()
    time.sleep(1)

    progress["value"] = 60
    root.update_idletasks()
    time.sleep(1)

    progress["value"] = 80
    root.update_idletasks()
    time.sleep(1)
    progress["value"] = 100


progress.pack(pady=10)

# This button will initialize
# the progress bar
Button(root, text="Start", command=bar).pack(pady=10)


# Importing required modules

import tkinter as tk
import tkinter.scrolledtext as st

# Creating tkinter window
win = tk.Tk()
win.title("ScrolledText Widget")

# Title Label
tk.Label(
    win,
    text="ScrolledText Widget Example",
    font=("Times New Roman", 15),
    background="green",
    foreground="white",
).grid(column=0, row=0)

# Creating scrolled text area
# widget with Read only by
# disabling the state
text_area = st.ScrolledText(win, width=30, height=8, font=("Times New Roman", 15))

text_area.grid(column=0, pady=10, padx=10)

# Inserting Text which is read only
text_area.insert(
    tk.INSERT,
    """\
This is a scrolledtext widget to make tkinter text read only.
Hi
Geeks !!!
Geeks !!!
Geeks !!!
Geeks !!!
Geeks !!!
Geeks !!!
Geeks !!!
""",
)

# Making the text read only
text_area.configure(state="disabled")
win.mainloop()

from tkinter import *

# create a root window.
top = Tk()

# create listbox object
listbox = Listbox(
    top,
    height=10,
    width=15,
    bg="grey",
    activestyle="dotbox",
    font="Helvetica",
    fg="yellow",
)

# Define the size of the window.
top.geometry("300x250")

# Define a label for the list.
label = Label(top, text=" FOOD ITEMS")

# insert elements by their
# index and names.
listbox.insert(1, "Nachos")
listbox.insert(2, "Sandwich")
listbox.insert(3, "Burger")
listbox.insert(4, "Pizza")
listbox.insert(5, "Burrito")

# pack the widgets
listbox.pack()
label.pack()


# Display until User
# exits themselves.
top.mainloop()


root.mainloop()
