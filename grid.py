# This imports all functions in tkinter module
from tkinter import *
from tkinter.ttk import *

# creating master window
master = Tk()

# This method is used to get the position
# of the desired widget available in any
# other widget
def click(event):

    # Here retrieving the size of the parent
    # widget relative to master widget
    x = event.x_root - f.winfo_rootx()
    y = event.y_root - f.winfo_rooty()

    # Here grid_location() method is used to
    # retrieve the relative position on the
    # parent widget
    z = f.grid_location(x, y)

    # printing position
    print(z)


# Frame widget, will work as
# parent for buttons widget
f = Frame(master)
f.pack()

# Button widgets
b = Button(f, text="Button")
b.grid(row=2, column=3)

c = Button(f, text="Button2")
c.grid(row=1, column=0)

# Here binding click method with mouse
master.bind("<Button-1>", click)

# infinite loop
mainloop()

# Importing tkinter module
from tkinter import *

# from tkinter.ttk import *

# creating Tk window
master = Tk()

# creating a Fra, e which can expand according
# to the size of the window
pane = Frame(master)
pane.pack(fill=BOTH, expand=True)

# button widgets which can also expand and fill
# in the parent widget entirely
# Button 1
b1 = Button(pane, text="Click me !", background="red", fg="white")
b1.pack(side=TOP, expand=True, fill=BOTH)

# Button 2
b2 = Button(pane, text="Click me too", background="blue", fg="white")
b2.pack(side=TOP, expand=True, fill=BOTH)

# Button 3
b3 = Button(pane, text="I'm also button", background="green", fg="white")
b3.pack(side=TOP, expand=True, fill=BOTH)

# Execute Tkinter
master.mainloop()
