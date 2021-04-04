from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json
#2

def encrypt_password(password):
    enc_nums = []
    print(password)
    for ch in password:
        enc = ord(ch)^23 # 23 is XOR key
        enc_nums.append(enc)

    print(enc_nums)

    with open("cyther.txt", "a") as data_file:
        data_file.write(f"{enc_nums} \n")
        print("crypt.txt file created or appended")


    encript_result.configure(text=password)


def find_password1():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
                data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

    # ---------------------------- UI SETUP ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    #pyperclip.copy(password)

    encrypt_password(password)

def read():
    with open("cyther.txt", "r") as data_file:
        data = data_file.readlines()

    index = 0
    for line in data:
        index += 1
        print(index,line)

def save2():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)



def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    save2()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                      f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
       # save2()

def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="apple.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)


#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=2, column=0)
encript_label = Label(text="Encripted:")
encript_label.grid(row=5, column=0)
encript_result = Label(text="******************")
encript_result.grid(row=5, column=1)

#Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "fizer@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)


# Buttons
generate_password_button = Button(text="Gen Pwd", command=generate_password)
generate_password_button.grid(row=4, column=0)
add_button = Button(text="Add",  command=save)
add_button.grid(row=4, column=1, columnspan=2)

add_button1 = Button(text="Read",  command=read)
add_button1.grid(row=4, column=2)


add_button2 = Button(text="JSON Find",  command=find_password1)
add_button2.grid(row=4, column=3)


















window.mainloop()