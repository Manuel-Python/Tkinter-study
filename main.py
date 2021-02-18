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

def spinbox_used():
    print(spinbox.get())

def scale_used(value):
    print(value)

def checkbutton_used():
    print(checked_state.get())

def radio_used():
    print(radio_state.get())

def listbox_used(event):
    print(listbox.get(listbox.curselection()))

spinbox = Spinbox(from_=0, to=100, width=5, command=spinbox_used)
spinbox.pack()

button = Button(text="Click Me", command=button_clicked)
button.pack()

input = Entry(width=10)
input.pack()
input

text = Text(height=5, width=30)
text.focus()
text.insert(END, "Multi-line text entry")
text.pack()

scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

checked_state = IntVar()
checkedbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checkedbutton.pack()

radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state,command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state,command=radio_used)
radiobutton3 = Radiobutton(text="Option3", value=3, variable=radio_state,command=radio_used)
radiobutton1.pack()
radiobutton2.pack()
radiobutton3.pack()

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]

for item in fruits:
    listbox.insert(fruits.index(item), item)

listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()
