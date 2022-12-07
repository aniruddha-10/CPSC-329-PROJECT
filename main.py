import base64
import os
import random
import string
import tkinter as tk
import sqlite3
import hashlib
from random import randint

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# Constants to specify necessary directories
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DB_DIR = os.path.join(ROOT_DIR, 'password_manager.db')
PNG_DIR = os.path.join(ROOT_DIR, '6fdf3511fd3fbdc1a5977e518207b930.png')

# Creating the Database for the Passwords
with sqlite3.connect("password_manager.db") as db:
    cursor = db.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS masterpassword(
id INTEGER  PRIMARY KEY,
password TEXT NOT NULL);
""")


# Intermediate functions

# Random password generation
# Returns a randomly generated password of type string.
def random_pass():
    char_types = ["sym", "num", "upper", "lower"]
    pass_len = 20
    password = ""
    # Looping to progressively add symbols to make a password of length 20
    # There is an equal chance of adding an uppercase character, a lowercase character, a number, or a symbol
    for i in range(0, pass_len):
        choice_index = randint(0, 3)
        choice = char_types[choice_index]
        if choice == "sym":
            symbol_list = string.punctuation
            symbol = symbol_list[randint(0, len(symbol_list)-1)]
            password = password+symbol
        elif choice == "num":
            num = randint(0, 9)
            password = password+str(num)
        elif choice == "upper":
            password = password+(random.choice(string.ascii_uppercase))
        else:
            password = password+(random.choice(string.ascii_lowercase))

    valid = isStrong(password)
    # If the password is invalid, make recursive call.
    if not valid[0]:
        random_pass()
    # Otherwise, return created password
    else:
        return password


# Function ensures attempted password strength.
# It must have an uppercase character, a lowercase character, a number, or a symbol
# It must have a minimum length of 10 characters
# Returns a list of boolean integers, where [0,0,0,0,0,0] Implies that:
# [0]: The password is invalid, [1]: The password is too short [2]: There are no uppercase characters
# [3]: There are no lowercase characters [4]: There are no numbers [5]: There are no symbols.
# If the code returned was [1,1,1,1,1,1], the opposite would be true for each condition.

def isStrong(password):
    return_code = [1, 0, 0, 0, 0, 0]

    if len(password) >= 10:
        return_code[1] = 1

    for i in range(0, len(password)):
        if password[i].isupper():
            return_code[2] = 1
        elif password[i].islower():
            return_code[3] = 1
        elif password[i].isdigit():
            return_code[4] = 1
        elif password[i] in string.punctuation:
            return_code[5] = 1

    # If any of the above conditions are not met, set validity to False
    for i in range(1, len(return_code)):
        if not return_code[i]:
            return_code[0] = 0

    return return_code


# Creates a new key from master password for encryption comparison
# Key is hashed with PBKDF2 HMAC-SHA256, Salted with os-generated random value.
# Hashed key and salt are stored separately in db for later use.
def new_key(x):
    x = x.encode()
    rand = os.urandom(16)
    salt = rand
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=400000)
    key = base64.urlsafe_b64encode(kdf.derive(x))
    insert_key = """INSERT INTO masterpassword(key) VALUES(?) """
    cursor.execute(insert_key, [key])
    db.commit()
    insert_salt = """INSERT INTO masterpassword(salt) VALUES(?) """
    cursor.execute(insert_salt, [salt])
    db.commit()


def hashing(x):
    hash = hashlib.sha256(x)
    hash = hash.hexdigest()
    return hash


# Main GUI
# Creating the main window
root = tk.Tk()


# Creating the GUI for when a new user
def initial_screen():
    root.title("Password Manager")
    canvas = tk.Canvas(root, height=500, width=500, bg="grey25")
    canvas.pack()
    frame = tk.Frame(root, bg="white")
    frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    tk.Label(root, text="Welcome to the Password Manager!", font=("Helvetica", 20, "bold"), bg="white",
             foreground="black").place(x=80, y=60)

    img = tk.PhotoImage(file="")
    tk.Label(root, image=img, border=0).place(x=180, y=90)

    tk.Label(root, text="Create a Master Password", font=("Arial", 14, "bold"), bg="white", foreground="Blue").place(
        x=155, y=225)
    txt = tk.Entry(border=0, show="*")
    txt.place(x=155, y=250)
    txt.focus()

    def show_password():
        if txt.cget("show") == "*":
            txt.config(show="")
        else:
            txt.config(show="*")

    tk.Checkbutton(root, text="Show Password", command=show_password, bg="white", foreground="black").place(x=155,
                                                                                                            y=280)

    tk.Label(root, text="Re-type your Password", font=("Arial", 14, "bold"), bg="white", foreground="Blue").place(x=155,
                                                                                                                  y=306)
    txt2 = tk.Entry(border=0, show="*")
    txt2.place(x=155, y=335)

    def show_password():
        if txt2.cget("show") == "*":
            txt2.config(show="")
        else:
            txt2.config(show="*")

    tk.Checkbutton(root, text="Show Password", command=show_password, bg="white", foreground="black").place(x=155,
                                                                                                            y=359)
    tk.Button(root, text="Close", font=("Bahnschrift 20", 14, "bold"), bg="white", foreground="black", borderwidth=2,
              command=quit).place(x=370, y=420)

    def save_passwords():
        if txt.get() == txt2.get():
            hashed = hashing(txt.get().encode("utf-8"))
            insert_pass = """INSERT INTO masterpassword(password)
            VALUES(?) """
            cursor.execute(insert_pass, [(hashed)])
            db.commit()
            password_manager()
        else:
            tk.Label(root, text="Passwords Don't Match", font=("Arial", 14, "bold"), bg="white",
                     foreground="Red").place(x=170, y=400)

    tk.Button(root, text="Submit", font=("Bahnschrift 20", 14, "bold"), bg="white", foreground="black", borderwidth=2,
              command=save_passwords).place(x=205, y=385)
    root.mainloop()


# Creating the GUI of the login screen
def login_screen():
    root.title("Password Manager")
    canvas = tk.Canvas(root, height=400, width=400, bg="#263D42")
    canvas.pack()
    frame = tk.Frame(root, bg="white")
    frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    tk.Label(root, text="Welcome to the Password Manager!", font=("Arial", 15, "bold"), bg="white",
             foreground="black").place(x=70, y=50)

    img = tk.PhotoImage(file=PNG_DIR)
    tk.Label(root, image=img, border=0).place(x=130, y=80)

    tk.Label(root, text="Enter Master Password", font=("Arial", 14, "bold"), bg="white", foreground="Red").place(x=120,
                                                                                                                 y=225)

    e3 = tk.Entry(border=0, show="*")
    e3.place(x=106, y=250)

    def show_password():
        if e3.cget("show") == "*":
            e3.config(show="")
        else:
            e3.config(show="*")

    tk.Checkbutton(root, text="Show Password", command=show_password, bg="white", foreground="black").place(x=104,
                                                                                                            y=275)

    def get_Master_Password():
        check_Hashed = hashing(e3.get().encode("utf-8"))
        cursor.execute("SELECT * FROM masterpassword WHERE id = 1 AND password = ?", [(check_Hashed)])
        return cursor.fetchall()

    def password_check():
        try:
            password = get_Master_Password()
            checking_pass = password[0]
            check = checking_pass[1]
            print(password)
            print(checking_pass)
            print(check)
            if hashing(e3.get().encode("utf-8")) == check:
                password_manager()
        except:
            tk.Label(root, text="Wrong Password", font=("Arial", 14, "bold"), bg="white", foreground="red").place(x=140,
                                                                                                                  y=340)

    tk.Button(root, text="Submit", font=("Bahnschrift 20", 14, "bold"), bg="white", foreground="black",
              command=password_check).place(x=160, y=305)
    tk.Button(root, text="Close", font=("Bahnschrift 20", 14, "bold"), bg="white", foreground="black", borderwidth=2,
              command=quit).place(x=280, y=330)

    root.mainloop()


# This lets the USER inside the Password Manager actually
def password_manager():
    for widget in root.winfo_children():
        widget.destroy()
    root.title("Password Manager")
    canvas = tk.Canvas(root, height=500, width=800, bg="#263D42")
    canvas.pack()
    frame = tk.Frame(root, bg="white")
    frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
    tk.Label(root, text="WELCOME TO THE PASSWORD VAULT, YOU CAN NOW STORE YOUR PASSWORDS!!", font=("Arial", 14, "bold"),
             bg="white", foreground="RED").place(x=115, y=80)

    def new_user():
        try:
            db.close()
            os.remove(DB_DIR)
            print("Please close the window and restart the program.")
        except FileNotFoundError:
            print("No such file found.")

    tk.Button(root, text="Switch User?", font=("Bahnschrift 20", 14, "bold"), bg="white", foreground="black",
              command=new_user).place(x=590, y=410)
    tk.Button(root, text="Close", font=("Bahnschrift 20", 14, "bold"), bg="white", foreground="black", borderwidth=2,
              command=quit).place(x=500, y=410)


cursor.execute("SELECT * FROM masterpassword")
if cursor.fetchall():
    login_screen()
else:
    initial_screen()
