import tkinter
from tkinter import *

w = tkinter.Tk()
w.title("PASSWORD MANAGER")
w.configure(bg="#333333")


def initial_window():
    w.geometry("400x300")
    Label(text="WELCOME TO PASSWORD MANAGER!", font=("Arial",18,"bold")).place(x=30,y=40)
    b1 = Button(w,text="NEW USER?",font=("Arial",20,"bold"),bg="yellow").place(x=100,y=100)
    b2 = Button(w,text="EXISTING USER?", font=("Arial", 20, "bold"),bg="yellow").place(x=80, y=180)
    
initial_window()
w.mainloop()
