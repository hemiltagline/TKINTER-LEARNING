# Importing tkinter module
from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk

# creating Tk window
# root = Tk()
# root.title("place method example")
# root.geometry("200x200")

# b2 = Button(root, text="GFG")
# b2.pack(fill=X, expand=True, ipady=10)

# # button widget
# b1 = Button(root, text="Click me !")
# b1.place(in_=b2, relx=0.5, rely=0.5, anchor=CENTER)

# # label widget
# l = Label(root, text="I'm a Label")
# l.place(anchor=NW)


master = Tk()

# this will create a label widget
l1 = Label(master, text="Height")
l2 = Label(master, text="Width")

# grid method to arrange labels in respective
# rows and columns as specified
l1.grid(row=0, column=0, sticky=W, pady=2)
l2.grid(row=1, column=0, sticky=W, pady=2)

# entry widgets, used to take entry from user
e1 = Entry(master)
e2 = Entry(master)

# this will arrange entry widgets
e1.grid(row=0, column=1, pady=2)
e2.grid(row=1, column=1, pady=2)

# checkbutton widget
c1 = Checkbutton(master, text="Preserve")
c1.grid(row=2, column=0, sticky=W, columnspan=2)

# adding image
image_path = r"/Users/mac/Desktop/projects/TKINTER-DEMO/images/cricket.jpeg"
img = Image.open(image_path)
img = img.resize((200, 200), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)

# setting image with the help of label
Label(master, image=img).grid(row=0, column=2, columnspan=2, rowspan=2, padx=5, pady=5)

# button widget
b1 = Button(master, text="Zoom in")
b2 = Button(master, text="Zoom out")

# arranging button widgets
b1.grid(row=2, column=2, sticky=E)
b2.grid(row=2, column=3, sticky=E)

# infinite loop which can be terminated
# by keyboard or mouse interrupt
mainloop()
