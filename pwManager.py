from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="apple.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)




















window.mainloop()