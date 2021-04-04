import requests

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude
iss_lat = 0.0
iss_long = 0.0


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the iss position.
    #if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
     #   return True
    return iss_latitude

print(is_iss_overhead())