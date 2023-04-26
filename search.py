# Python Program to search string in text using Tkinter

from tkinter import *

root = Tk()
fram = Frame(root)
Label(fram, text="Text to find:").pack(side=LEFT)
edit = Entry(fram)
edit.pack(side=LEFT, fill=BOTH, expand=1)
edit.focus_set()
butt = Button(fram, text="Find")
butt.pack(side=RIGHT)
fram.pack(side=TOP)


text = Text(root)
text.insert("1.0", """Type your text here""")
text.pack(side=BOTTOM)


def find():

    text.tag_remove("found", "1.0", END)
    s = edit.get()
    if s:
        idx = "1.0"
        while 1:
            idx = text.search(s, idx, nocase=1, stopindex=END)
            if not idx:
                break
            lastidx = "%s+%dc" % (idx, len(s))
            text.tag_add("found", idx, lastidx)
            idx = lastidx
    text.tag_config("found", foreground="red")
    edit.focus_set()


butt.config(command=find)


def callback(input):

    if input.isdigit():
        print(input)
        return True

    elif input is "":
        print(input)
        return True

    else:
        print(input)
        return False


root = Tk()

e = Entry(root)
e.place(x=50, y=50)
reg = root.register(callback)

e.config(validate="key", validatecommand=(reg, "% P"))

root.mainloop()
