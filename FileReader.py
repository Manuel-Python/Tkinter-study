


from tkinter import *

data = ""

def read_file():
    with open("data.csv") as data_file:
        data = data_file.read()
        text.delete('1.0', END)
        text.insert(END,data)


        labNum = len(data)
        kilometer_result_label.config(text=f"{labNum}")

window = Tk()
window.title("Read data File")
window.config(padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.grid(column=1 , row=0)

miles_label = Label(text="CSV")
miles_label.grid(column=2 , row=0 )

is_equal_label = Label(text="File Data")
is_equal_label.config(padx=1, pady=-50)
is_equal_label.grid(column=0 , row=3 )

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1 , row=1 )

kilometer_label = Label(text="File Count")
kilometer_label.grid(column=0, row=1 )

calculate_button = Button(text="Read File", command=read_file)
calculate_button.grid(column=1 , row=2 )

text = Text(height=5, width=30)
text.focus()
text.insert(END, "Multi-line text entry")
text.grid(column=1,row=4)



window.mainloop()