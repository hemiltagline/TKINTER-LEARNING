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
b1.pack(side=LEFT, expand=True, fill=BOTH)

# Button 2
b2 = Button(pane, text="Click me too", background="blue", fg="white")
b2.pack(side=LEFT, expand=True, fill=BOTH)

# Button 3
b3 = Button(pane, text="I'm also button", background="green", fg="white")
b3.pack(side=LEFT, expand=True, fill=BOTH)

# Execute Tkinter
master.mainloop()

# Import all files from
# tkinter and overwrite
# all the tkinter files
# by tkinter.ttk
from tkinter import *
from tkinter.ttk import *

# creates tkinter window or root window
root = Tk()
root.geometry("200x100")

# function to be called when mouse enters in a frame
def enter(event):
    print("Button-2 pressed at x = % d, y = % d" % (event.x, event.y))


# function to be called when mouse exits the frame
def exit_(event):
    print("Button-3 pressed at x = % d, y = % d" % (event.x, event.y))


# frame with fixed geometry
frame1 = Frame(root, height=100, width=200)

# these lines are showing the
# working of bind function
# it is universal widget method
frame1.bind("<Enter>", enter)
frame1.bind("<Leave>", exit_)

frame1.pack()

mainloop()
