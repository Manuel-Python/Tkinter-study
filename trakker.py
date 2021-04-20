from tkinter import *

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


def read_file():
    with open("position.txt") as data_file:
        data = data_file.read()
        text.delete('1.0', END)
        text.insert(END,data)



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

text = Text(height=5, width=30)
text.focus()
text.insert(END, "File data goes here")
text.grid(column=0,row=3, columnspan=3)





window.mainloop()

