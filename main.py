#import tkinter    1
from tkinter import *




window = Tk()

window.title("Tkinter demo")
window.minsize(width=500, height=500)

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New text"
my_label.config(text="More new text")

def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)

button = Button(text="Click Me", command=button_clicked)
button.pack()

input = Entry(width=10)
input.pack()
input

window.mainloop()
