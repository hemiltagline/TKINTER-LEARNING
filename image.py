import tkinter
from PIL import ImageTk, Image
from tkinter import *

root = tkinter.Tk()
root.title("Working with image in Tkinter")

img = ImageTk.PhotoImage(Image.open("images/cricket1.jpeg"))

label = tkinter.Label(root, image=img)
label.pack()


canvas = tkinter.Canvas(root, width=500, height=250)

canvas.pack()

img1 = ImageTk.PhotoImage(Image.open("images/book_cover1.jpeg"))

canvas.create_image(135, 20, image=img1)


# Set Title as Image Loader
root.title("Image Loader")

# Set the resolution of window
root.geometry("550x300 + 300 + 150")

# Allow Window to be resizable
root.resizable(width=True, height=True)

# Create a button and place it into the window using grid layout
btn = Button(root, text="open image", image=img1).grid(row=1, columnspan=4)

root.mainloop()
