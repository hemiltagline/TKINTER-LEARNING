# Importing Tkinter module
from tkinter import *

from tkinter.ttk import *

# Creating master Tkinter window
root = Tk()
root.geometry("175x175")

values = {
    "RadioButton 1": "1",
    "RadioButton 2": "2",
    "RadioButton 3": "3",
    "RadioButton 4": "4",
    "RadioButton 5": "5",
}
selected_value = StringVar()
for (text, value) in values.items():
    # Associate each radio button with the same variable
    Radiobutton(
        root,
        text=text,
        variable=selected_value,
        value=value,
    ).pack(fill=X, ipady=5)


w = Label(root, text="Select Your hobby", font="50")
w.pack()

Checkbutton1 = IntVar()
Checkbutton2 = IntVar()
Checkbutton3 = IntVar()

Button1 = Checkbutton(
    root,
    text="Tutorial",
    variable=Checkbutton1,
    onvalue=1,
)

Button2 = Checkbutton(
    root,
    text="Student",
    variable=Checkbutton2,
    onvalue=1,
)

Button3 = Checkbutton(
    root,
    text="Courses",
    variable=Checkbutton3,
    onvalue=1,
)

Button1.pack()
Button2.pack()
Button3.pack()
root.mainloop()
