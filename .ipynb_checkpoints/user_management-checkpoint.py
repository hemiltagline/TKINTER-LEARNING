import tkinter as tk

# create an array to store user data
users = []

# define a function to insert a new user into the array
def insert_user():
    # get the values from the input fields
    username = username_entry.get()
    password = password_entry.get()
    email = email_entry.get()
    # add the values to the users array
    users.append((username, password, email))
    # clear the input fields
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

# define a function to update an existing user in the array
def update_user():
    # get the index of the user to update
    index = int(index_entry.get())
    # get the new values from the input fields
    username = username_entry.get()
    password = password_entry.get()
    email = email_entry.get()
    # update the user in the users array
    users[index] = (username, password, email)
    # clear the input fields
    index_entry.delete(0, tk.END)
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

# define a function to delete an existing user from the array
def delete_user():
    # get the index of the user to delete
    index = int(index_entry.get())
    # delete the user from the users array
    del users[index]
    # clear the input fields
    index_entry.delete(0, tk.END)

# create a Tkinter window
window = tk.Tk()

# create input fields for the user data
tk.Label(window, text="Username").grid(row=0, column=0)
username_entry = tk.Entry(window)
username_entry.grid(row=0, column=1)
tk.Label(window, text="Password").grid(row=1, column=0)
password_entry = tk.Entry(window)
password_entry.grid(row=1, column=1)
tk.Label(window, text="Email").grid(row=2, column=0)
email_entry = tk.Entry(window)
email_entry.grid(row=2, column=1)

# create input fields for the index of the user to update/delete
tk.Label(window, text="Index").grid(row=3, column=0)
index_entry = tk.Entry(window)
index_entry.grid(row=3, column=1)

# create buttons for the insert/update/delete operations
tk.Button(window, text="Insert", command=insert_user).grid(row=4, column=0)
tk.Button(window, text="Update", command=update_user).grid(row=4, column=1)
tk.Button(window, text="Delete", command=delete_user).grid(row=4, column=2)

# start the Tkinter event loop
window.mainloop()
