from tkinter import *
import os
import requests
import smtplib



MY_EMAIL = "___YOUR_EMAIL_HERE____"
MY_PASSWORD = "___YOUR_PASSWORD_HERE___"

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude
iss_lat = 0.0
iss_long = 0.0

positionISS = []

def send_email(message):
        connection = smtplib.SMTP("__YOUR_SMTP_ADDRESS_HERE___")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject: Test Email\n" + message
        )


def save(position):
    with open("position.txt", "a") as data_file:
        data_file.write(f"{position[0]} , {position[1]} \n")

def iss_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    iss_loc = (iss_latitude, iss_longitude)


    return iss_loc

def generate_location():
    for n in range(20):
        a = iss_position()
        save(a)
        positionISS.append(a)

    s = ""
    for x in positionISS:
        string = f"{x[0]} {x[1]}"
        s += string

    # send_email(s)
    print(positionISS)

def new_file():
    with open("position.txt", "a") as data_file:
        pass


def read_file():
    with open("position.txt") as data_file:
        data = data_file.read()
        text.delete('1.0', END)
        text.insert(END,data)


def del_file():
    if os.path.isfile("position.txt"):
        os.remove("position.txt")

def clear_text():
    text.delete('1.0', END)

def analyse_file():
    lineNums = 0
    with open("position.txt") as data_file:
        for line in data_file:
            lineNums += 1
            print(lineNums)
            data = data_file.readline()

    text.delete('1.0', END)
    text.insert(END, f"Number of lines {lineNums}")


def new_window():
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(window)

    # sets the title of the
    # Toplevel widget
    newWindow.title("New Window")

    # sets the geometry of toplevel
    newWindow.geometry("200x200")

    # A Label widget to show in toplevel
    Label(newWindow,
          text="This is a new window").pack()

def change_image():
    logo_img = PhotoImage(file="tomato.png")
    canvas.create_image(100, 100, image=logo_img)
    canvas.image_names(logo_img)

def dir_listing():
    dir_list = os.listdir("/")
    text_list = ""
    for d in dir_list:
        text_list += f"{d}, "

    text.delete('1.0', END)
    text.insert(END, f" {text_list}")
    #print(os.listdir("/"))

def files_listing():
    file_list = os.listdir()

    text_list = ""
    for d in file_list:
        if d.endswith(".py"):
            text_list += f"{d}, "

    text.delete('1.0', END)
    text.insert(END, f" {text_list}")



window = Tk()
window.title("ISS Tracker")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="apple.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)


#Labels
website_label = Label(text="ISS Tracker:")
website_label.grid(row=1, column=0)

pos_label = Label(text="Lat / Long")
pos_label.grid(row=1, column=1)


loc_button = Button(text="Gen Loc", command=generate_location)
loc_button.grid(row=2, column=0)

read_button = Button(text="Read File", command=read_file)
read_button.grid(row=2, column=1)

del_button = Button(text="Delete File", command=del_file)
del_button.grid(row=2, column=2)

new_button = Button(text="New File", command=new_file)
new_button.grid(row=2, column=3)

analyse_button = Button(text="Analyse File", command=analyse_file)
analyse_button.grid(row=3, column=3)


new_button = Button(text="New Window", command=new_window)
new_button.grid(row=4, column=3)


send_button = Button(text="Email", command=send_email)
send_button.grid(row=4, column=0)

tmp_button = Button(text="Other", command=send_email)
tmp_button.grid(row=4, column=2)


clear_button = Button(text="Clear", command=clear_text)
clear_button.grid(row=4, column=1)

other_button = Button(text="Image", command=change_image)
other_button.grid(row=0, column=2)

direct_button = Button(text="Directory", command=dir_listing)
direct_button.grid(row=0, column=3)

dir_button = Button(text="Files Dir", command=files_listing)
dir_button.grid(row=0, column=4)

text = Text(height=5, width=60)
text.focus()
text.insert(END, "File data goes here")
text.grid(column=0,row=3, columnspan=2)





window.mainloop()

