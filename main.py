import os
import tkinter as tk
import sqlite3
import hashlib
from tkinter import simpledialog
from functools import partial

# Creating the Database for the Passwords
with sqlite3.connect("password_manager.db") as db:
    cursor = db.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS masterpassword(
id INTEGER  PRIMARY KEY,
password TEXT NOT NULL);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS passwordmanager(
id INTEGER  PRIMARY KEY,
website TEXT NOT NULL,
username TEXT NOT NULL,
password TEXT NOT NULL);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS userpasswords(
id INTEGER  PRIMARY KEY,
passwords TEXT NOT NULL);
""")



# for the popup
def popupbox(text):
    answer = simpledialog.askstring("Input String", text)
    return answer

# Creating the main window
root = tk.Tk()


def hashing(x):
    hash = hashlib.sha256(x)
    hash = hash.hexdigest()
    return hash

# Creating the GUI for when a new user
def initial_screen():
    root.title("Password Manager")
    canvas = tk.Canvas(root, height=500, width=500, bg="grey25")
    canvas.pack()
    frame = tk.Frame(root, bg="white")
    frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    tk.Label(root, text="Welcome to the Password Manager!", font=("Helvetica", 20, "bold"), bg="white",foreground="black").place(x=80, y=60)

    img = tk.PhotoImage(file="/Users/aniruddhakhan/Desktop/CPSC PROJECT/6fdf3511fd3fbdc1a5977e518207b930.png")
    tk.Label(root, image=img, border=0).place(x=180, y=90)

    tk.Label(root, text="Create a Master Password", font=("Arial", 14, "bold"), bg="white", foreground="Blue").place(x=155, y=225)
    txt = tk.Entry(border=0, show="*")
    txt.place(x=155, y=250)
    txt.focus()

    def show_password():
        if (txt.cget("show") =="*"):
            txt.config(show="")
        else:
            txt.config(show="*")
    tk.Checkbutton(root, text="Show Password",command=show_password,bg="white",foreground="black").place(x=155,y=280)


    tk.Label(root, text="Re-type your Password", font=("Arial", 14, "bold"), bg="white", foreground="Blue").place(x=155, y=306)
    txt2 = tk.Entry(border=0,show="*")
    txt2.place(x=155,y=335)

    def show_password():
        if (txt2.cget("show") =="*"):
            txt2.config(show="")
        else:
            txt2.config(show="*")
    tk.Checkbutton(root, text="Show Password",command=show_password,bg="white",foreground="black").place(x=155,y=359)
    tk.Button(root, text="Close",font=("Bahnschrift 20", 14,"bold"), bg="white",foreground="black",borderwidth=2,command=quit).place(x=370,y=420)


    def save_passwords():
        if (txt.get() == txt2.get()):
            hashed = hashing(txt.get().encode("utf-8"))
            insert_pass = """INSERT INTO masterpassword(password)
            VALUES(?) """
            cursor.execute(insert_pass,[(hashed)])
            db.commit()
            password_manager()
        else:
            tk.Label(root, text="Passwords Don't Match", font=("Arial", 14, "bold"), bg="white", foreground="Red").place(x=170, y=400)

    tk.Button(root, text="Submit",font=("Bahnschrift 20", 14,"bold"), bg="white",foreground="black",borderwidth=2,command=save_passwords).place(x=205,y=385)
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

    e3 = tk.Entry(border=0,show="*")
    e3.place(x=106,y=250)

    def show_password():
        if (e3.cget("show") == "*"):
            e3.config(show="")
        else:
            e3.config(show="*")

    tk.Checkbutton(root, text="Show Password", command=show_password, bg="white", foreground="black").place(x=104,y=275)


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
            tk.Label(root,text="Wrong Password",font=("Arial",14,"bold"),bg="white",foreground="red").place(x=140,y=340)

    tk.Button(root, text="Submit", font=("Bahnschrift 20",14,"bold"), bg="white",foreground="black",command=password_check).place(x=160,y=305)
    tk.Button(root, text="Close",font=("Bahnschrift 20", 14,"bold"), bg="white",foreground="black",borderwidth=2,command=quit).place(x=280,y=330)

    root.mainloop()

# This lets the USER inside the Password Manager actually
def password_manager():
    for widget in root.winfo_children():
        widget.destroy()
    root.title("Password Manager")

    def add_entry():
        text1 = "Website"
        text2 = "Username"
        text3 = "Password"

        website = popupbox(text1)
        username = popupbox(text2)
        password = popupbox(text3)

        hashed_pass = hashing(password.encode("utf-8"))

        insert_fields ="""INSERT INTO passwordmanager(website,username,password)
        VALUES(?, ?, ?)"""

        insert_password ="""INSERT INTO userpasswords(passwords)
        VALUES(?)"""

        cursor.execute(insert_fields,(website,username,password))

        cursor.execute(insert_password,[(hashed_pass)])

        db.commit()
        password_manager()

    root.geometry("780x340")

    lb = tk.Label(root, text="Welcome to the Password Manager!!",font=("Arial",18,"bold"),foreground="RED")
    lb.grid(column=1,padx=120)
    but = tk.Button(root, text="ADD",font=("Arial",13,"bold"),bg="white",foreground="Green",command=add_entry)
    but.grid(column=1,row=2)

    def remove_entry(input):
        cursor.execute("DELETE FROM passwordmanager where id = ?", (input,))
        db.commit()
        password_manager()


    def new_user():
        path ="/Users/aniruddhakhan/Desktop/pythonProject/password_manager.db"
        try:
            os.remove(path)
            print("Now CLose the Window and Restart the Program")
        except FileNotFoundError:
            print("No such File found")

    # tk.Button(root, text="Switch User?", font=("Bahnschrift 20",14,"bold"), bg="white",foreground="black",command=new_user).place(x=590,y=410)
    # tk.Button(root, text="Close",font=("Bahnschrift 20", 14,"bold"), bg="white",foreground="black",borderwidth=2,command=quit).place(x=500,y=410)

    lbl = tk.Label(root, text = "WEBSITE", font=("Arial",13,"bold"),foreground="white")
    lbl.grid(row=3,column=0)
    lbl = tk.Label(root, text="USERNAME", font=("Arial", 13, "bold"), foreground="white")
    lbl.grid(row=3, column=1)
    lbl = tk.Label(root, text="PASSWORD", font=("Arial", 13, "bold"),foreground="white")
    lbl.grid(row=3, column=2)
    cursor.execute("SELECT * FROM passwordmanager")

    try:
        if(cursor.fetchall() != None):
            i = 0
            while True:
                cursor.execute("SELECT * FROM passwordmanager")
                array = cursor.fetchall()
                lbl1 = tk.Label(root, text=(array[i][1]), font=("Arial", 13,),foreground="white")
                lbl1.grid(column=0,row=i+4)
                lbl1 = tk.Label(root, text=(array[i][2]), font=("Arial", 13,), foreground="white")
                lbl1.grid(column=1, row=i + 4)
                lbl1 = tk.Label(root, text=(array[i][3]), font=("Arial", 13,), foreground="white")
                lbl1.grid(column=2, row=i + 4)
                button = tk.Button(root, text="delete",command=partial(remove_entry,array[i][0]))
                button.grid(column=3, row=i+4)
                i = i + 1
                cursor.execute("SELECT * FROM passwordmanager")
                if(len(cursor.fetchall())<=1):
                    break
    except:
        print("Keep Calm and Store Passwords")

cursor.execute("SELECT * FROM masterpassword")
if cursor.fetchall():
    login_screen()
else:
    initial_screen()
