from tkinter import *
from tkinter.ttk import *  # This will give you the effects of modern graphics
import requests

root = Tk()

# Create example window
root.title("Example window")
root.geometry("100x100")

style = Style()

style.configure("W.TButton", foreground="red")

url = "https://www.dyvak.com/static/images/logo/dyvak-logo.png"
response = requests.get(url)
img_data = response.content

photo = PhotoImage(data=img_data)

btn1 = Button(root, text="Quit !", style="W.TButton", command=root.destroy)
btn1.grid(row=0, padx=900)

button = Button(text="Close this window", command=root.destroy)
button.grid(row=1, padx=900)

# the label for user_name
user_name = Label(root, text="Username").place(x=40, y=60)

# the label for user_password
user_password = Label(root, text="Password").place(x=40, y=100)

submit_button = Button(root, text="Submit").place(x=40, y=130)

user_name_input_area = Entry(root, width=30).place(x=110, y=60)

user_password_entry_area = Entry(root, width=30).place(x=110, y=100)

# label_frame = LabelFrame(root, text="This is Label Frame")
# label_frame.pack(expand="yes", fill="both")

# label1 = Label(label_frame, text="1. This is a Label.")
# label1.place(x=0, y=5)

# label2 = Label(label_frame, text="2. This is another Label.")
# label2.place(x=0, y=35)

# label3 = Label(label_frame, text="3. We can add multiple\n    widgets in it.")

# label3.place(x=0, y=65)

our_canvas = Canvas(root, width=300, height=200, bg="white")
our_canvas.pack()
# creating rectangle
our_canvas.create_rectangle(50, 150, 250, 50, fill="blue")

root.mainloop()
