# from tkinter import *
# from tkinter.ttk import *

# # creates tkinter window or root window
# root = Tk()
# root.geometry("200x100")

# # function to be called when mouse enters in a frame
# def enter(event):
#     print("Button-2 pressed at x = % d, y = % d" % (event.x, event.y))


# # function to be called when mouse exits the frame
# def exit_(event):
#     print("Button-3 pressed at x = % d, y = % d" % (event.x, event.y))


# # frame with fixed geometry
# frame1 = Frame(root, height=100, width=200)

# # these lines are showing the
# # working of bind function
# # it is universal widget method
# frame1.bind("<Enter>", enter)
# frame1.bind("<Leave>", exit_)

# frame1.pack()

# mainloop()
from tkinter import *


def go():
    cs = Lb.curselection()

    # Updating label text to selected option
    w.config(text=Lb.get(cs))

    # Setting Background Colour
    for list in cs:

        if list == 0:
            top.configure(background="red")
        elif list == 1:
            top.configure(background="green")
        elif list == 2:
            top.configure(background="yellow")
        elif list == 3:
            top.configure(background="white")


top = Tk()
top.geometry("250x275")
top.title("Double Click")

# Creating Listbox
Lb = Listbox(top, height=6)
# Inserting items in Listbox
Lb.insert(0, "Red")
Lb.insert(1, "Green")
Lb.insert(2, "Yellow")
Lb.insert(3, "White")

# Binding double click with left mouse
# button with go function
Lb.bind("<Double-1>", lambda event: go())
Lb.pack()

# Creating Edit box to show selected option
w = Label(top, text="Default")
w.pack()
top.mainloop()
