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


window = Tk()
window.title("ISS Tracker")
window.config(padx=20, pady=20)

#Labels
website_label = Label(text="ISS Tracker:")
website_label.grid(row=1, column=0)


for n in range(20):
    a = iss_position()
    save(a)
    positionISS.append(a)




s=""
for x in positionISS:
    string = f"{x[0]} {x[1]}"
    s+= string

#send_email(s)
print(positionISS)

window.mainloop()

