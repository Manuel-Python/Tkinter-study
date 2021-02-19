#import tkinter    1
from tkinter import *




window = Tk()

window.title("Tkinter demo")
window.minsize(width=500, height=500)
window.config(padx=100, pady=200)

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
#my_label.pack()
#my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)
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
#spinbox.pack()
spinbox.grid(column=2, row=2)

button = Button(text="Click Me", command=button_clicked)
button.grid(column=3,row=3)

input = Entry(width=10)
#input.pack()
input

text = Text(height=5, width=30)
text.focus()
text.insert(END, "Multi-line text entry")
text.grid(column=4,row=4)

scale = Scale(from_=0, to=100, command=scale_used)
scale.grid(column=4,row=5)

checked_state = IntVar()
checkedbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checkedbutton.grid(column=2,row=0)

radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state,command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state,command=radio_used)
radiobutton3 = Radiobutton(text="Option3", value=3, variable=radio_state,command=radio_used)
radiobutton1.grid(column=2,row=2)
radiobutton2.grid(column=2,row=3)
radiobutton3.grid(column=2,row=4)

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]

for item in fruits:
    listbox.insert(fruits.index(item), item)

listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.grid(column=5,row=0)

window.mainloop()
