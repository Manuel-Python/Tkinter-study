
import requests




MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude
iss_lat = 0.0
iss_long = 0.0

positionISS = []

def save(position):
    with open("position.txt", "a") as data_file:
        data_file.write(f"{position[0]} | {position[1]} \n")

def iss_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    iss_loc = (iss_latitude, iss_longitude)


    return iss_loc

for n in range(200):
    a = iss_position()
    save(a)
    positionISS.append(a)

print(positionISS)

