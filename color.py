from tkinter import *
from tkinter import colorchooser

# Function that will be invoked when the
# button will be clicked in the main window
def choose_color():

    # variable to store hexadecimal code of color
    color_code = colorchooser.askcolor(title="Choose color")
    print(color_code)


root = Tk()
button = Button(root, text="Select color", command=choose_color)
button.pack()
root.geometry("300x300")

from tkinter.ttk import *

# getting screen's height in pixels
height = root.winfo_screenheight()

# getting screen's width in pixels
width = root.winfo_screenwidth()

print("\n width x height = %d x %d (in pixels)\n" % (width, height))

# Adjust size
root.geometry("200x200")

# Set Label
root = Label(text="Splash Screen", font=18)
root.pack()


def main():
    # Create object
    root = Tk()

    # Adjust size
    root.geometry("400x400")


main()

from tkinter import ttk

text1 = StringVar()
text2 = StringVar()

# These text are used to set initial
# values of Checkbutton to off
text1.set("OFF")
text2.set("OFF")

chkbtn1 = ttk.Checkbutton(
    root,
    textvariable=text1,
    variable=text1,
    offvalue="GFG Not Selected",
    onvalue="GFG Selected",
)

chkbtn1.pack(side=TOP, pady=10)
chkbtn2 = ttk.Checkbutton(
    root, textvariable=text2, variable=text2, offvalue="GFG Average", onvalue="GFG Good"
)
chkbtn2.pack(side=TOP, pady=10)

root.mainloop()
