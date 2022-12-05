import os
import tkinter as tk
import sqlite3
import hashlib

# Creating the Database for the Passwords
with sqlite3.connect("password_manager.db") as db:
    cursor = db.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS masterpassword(
id INTEGER  PRIMARY KEY,
password TEXT NOT NULL);
""")

# Creating the main window
root = tk.Tk()

def hashing(x):
    hash = hashlib.sha256(x)
    hash = hash.hexdigest()
    return hash

# Creatingg the GUI for when a new user
def initial_screen():
    root.title("Password Manager")
    canvas = tk.Canvas(root, height=500, width=500, bg="DarkOrchid3")
    canvas.pack()
    frame = tk.Frame(root, bg="white")
    frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    tk.Label(root, text="Welcome to the Password Manager!", font=("Helvetica", 20, "bold"), bg="white",foreground="black").place(x=80, y=60)

    img = tk.PhotoImage(file="/Users/aniruddhakhan/Desktop/CPSC PROJECT/6fdf3511fd3fbdc1a5977e518207b930.png")
    tk.Label(root, image=img, border=0).place(x=180, y=90)

    tk.Label(root, text="Create a Master Password", font=("Arial", 14, "bold"), bg="white", foreground="Blue").place(x=155, y=225)
    txt = tk.Entry(border=0)
    txt.place(x=155, y=250)
    txt.focus()

    tk.Label(root, text="Re-type your Password", font=("Arial", 14, "bold"), bg="white", foreground="Blue").place(x=155, y=290)
    txt2 = tk.Entry(border=0)
    txt2.place(x=155,y=315)

    def save_passwords():
        if (txt.get() == txt2.get()):
            hashed = hashing(txt.get().encode("utf-8"))
            insert_pass = """INSERT INTO masterpassword(password)
            VALUES(?) """
            cursor.execute(insert_pass,[(hashed)])
            db.commit()
            password_manager()
        else:
            tk.Label(root, text="Passwords Don't Match", font=("Arial", 14, "bold"), bg="white", foreground="Red").place(x=170, y=380 )

    tk.Button(root, text="Submit",font=("Bahnschrift 20", 14,"bold"), bg="white",foreground="black",borderwidth=2,command=save_passwords).place(x=205,y=349)
    root.mainloop()


# Creating the GUI of the login screen
def login_screen():
    root.title("Password Manager")
    canvas = tk.Canvas(root, height=400, width=400, bg="#263D42")
    canvas.pack()
    frame = tk.Frame(root, bg="white")
    frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    tk.Label(root, text="Welcome to the Password Manager!",font=("Arial",15,"bold"),bg="white",foreground="black").place(x=70,y=50)

    img = tk.PhotoImage(file="/Users/aniruddhakhan/Desktop/CPSC PROJECT/6fdf3511fd3fbdc1a5977e518207b930.png")
    tk.Label(root, image=img, border=0).place(x=130, y=80)

    tk.Label(root,text="Enter Master Password",font=("Arial",14,"bold"),bg="white",foreground="Red").place(x=120,y=225)

    e3 = tk.Entry(border=0)
    e3.place(x=106,y=250)

    def get_Master_Password():
        check_Hashed = hashing(e3.get().encode("utf-8"))
        cursor.execute("SELECT * FROM masterpassword WHERE id = 1 AND password = ?",[(check_Hashed)])
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
            tk.Label(root,text="Wrong Password",font=("Arial",14,"bold"),bg="white",foreground="red").place(x=140,y=310)

    tk.Button(root, text="Submit", font=("Bahnschrift 20",14,"bold"), bg="white",foreground="black",command=password_check).place(x=160,y=280)
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
    tk.Label(root, text="WELCOME TO THE PASSWORD VAULT, YOU CAN NOW STORE YOUR PASSWORDS!!",font=("Arial",14,"bold"),bg="white",foreground="RED").place(x=115,y=80)

    def new_user():
        path ="/Users/aniruddhakhan/Desktop/pythonProject/password_manager.db"
        try:
            os.remove(path)
            print("Now CLose the Window and Restart the Program")
        except FileNotFoundError:
            print("No such File found")

    tk.Button(root, text="Switch User?", font=("Bahnschrift 20",14,"bold"), bg="white",foreground="black",command=new_user).place(x=550,y=410)

cursor.execute("SELECT * FROM masterpassword")
if cursor.fetchall():
    login_screen()
else:
    initial_screen()
