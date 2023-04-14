from tkinter import *
import sqlite3


class RegisterLogin:
    def __init__(self, master):
        self.master = master
        self.master.title("Register/Login")

        # Create a database connection
        self.conn = sqlite3.connect("users.db")
        self.cursor = self.conn.cursor()
        # Create a table for storing user information
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS users 
                            (id INTEGER PRIMARY KEY, username TEXT, password TEXT)"""
        )
        self.conn.commit()

        # Create and pack the register and login frames
        self.register_frame = Frame(self.master)
        self.login_frame = Frame(self.master)
        self.register_frame.pack(pady=10)
        self.login_frame.pack(pady=10)

        # Create and pack widgets for the register frame
        Label(self.register_frame, text="Register", font=("Helvetica", 16)).pack()
        Label(self.register_frame, text="Username").pack(pady=5)
        self.register_username_entry = Entry(self.register_frame)
        self.register_username_entry.pack()
        Label(self.register_frame, text="Password").pack(pady=5)
        self.register_password_entry = Entry(self.register_frame, show="*")
        self.register_password_entry.pack()
        Button(self.register_frame, text="Register", command=self.create_user).pack(
            pady=10
        )

        # Create and pack widgets for the login frame
        Label(self.login_frame, text="Login", font=("Helvetica", 16)).pack()
        Label(self.login_frame, text="Username").pack(pady=5)
        self.login_username_entry = Entry(self.login_frame)
        self.login_username_entry.pack()
        Label(self.login_frame, text="Password").pack(pady=5)
        self.login_password_entry = Entry(self.login_frame, show="*")
        self.login_password_entry.pack()
        Button(self.login_frame, text="Login", command=self.read_user).pack(pady=10)

    def create_user(self):
        username = self.register_username_entry.get()
        password = self.register_password_entry.get()
        # Insert the username and password into the database
        self.cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)", (username, password)
        )
        self.conn.commit()
        print(f"Registered username: {username}, password: {password}")

    def read_user(self):
        username = self.login_username_entry.get()
        password = self.login_password_entry.get()
        # Retrieve the user with the given username and password from the database
        self.cursor.execute(
            "SELECT * FROM users WHERE username=? AND password=?", (username, password)
        )
        user = self.cursor.fetchone()
        if user is not None:
            print(f"Login successful for user with id {user[0]}")
            # Update the user's password
            self.update_user(user[0], "newpassword")
            # Delete the user
            self.delete_user(user[0])
        else:
            print("Login failed")

    def update_user(self, user_id, new_password):
        # Update the user's password in the database
        self.cursor.execute(
            "UPDATE users SET password=? WHERE id=?", (new_password, user_id)
        )
        self.conn.commit()
        print(f"Updated password for user with id {user_id}")

    def delete_user(self, user_id):
        # Delete the user from the database
        self.cursor.execute("DELETE FROM users WHERE id=?", (user_id,))
        self.conn.commit()
        print(f"Deleted user with id {user_id}")

    def __del__(self):
        # Close the database connection when the object is destroyed
        self.conn.close


root = Tk()
register_login = RegisterLogin(root)
root.mainloop()
