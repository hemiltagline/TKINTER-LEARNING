# Python program demonstrating
# Multiple selection in Listbox widget


from tkinter import *

root = Tk()
root.title("Multi selection")
root.geometry("100x150")

list = Listbox(root, selectmode="multiple")

list.pack()

x = ["C", "C++", "Java", "Python", "R", "Go", "Ruby", "JavaScript", "Swift"]

for each_item in range(len(x)):
    list.insert(END, x[each_item])
    list.itemconfig(each_item, bg="green" if each_item % 2 == 0 else "cyan")

root.mainloop()
