


from tkinter import *

def read_file():
    with open("data.csv") as data_file:
        data = data_file.read()

        print(data)

window = Tk()
window.title("Read data File")
window.config(padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.grid(column=1 , row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2 , row=0 )

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0 , row=1 )

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1 , row=1 )

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1 )

calculate_button = Button(text="Read File", command=read_file)
calculate_button.grid(column=1 , row=2 )

text = Text(height=5, width=30)
text.focus()
text.insert(END, "Multi-line text entry")
text.grid(column=1,row=4)



window.mainloop()