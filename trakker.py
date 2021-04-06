import pygal as pygal
import requests
import pygal

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude
iss_lat = 0.0
iss_long = 0.0


def iss_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    iss_loc = (iss_latitude, iss_longitude)


    return iss_loc

for n in range(20):
    print(iss_position())


# import Style class from pygal.style
from pygal.style import Style

# create a Style object
custom_style = Style(colors=('#FF0000', '#0000FF',
                             '#00FF00', '#000000',
                             '#FFD700'))

# create a world map,
# Style class is used for using
# the custom colours in the map,
worldmap = pygal.maps.world.World(style
                                  =custom_style)

# set the title of the map
worldmap.title = 'Some Countries Starting from Specific Letters'

# hex code of colours are used
# for every .add() called
worldmap.add('"E" Countries',
             ['ec', 'ee', 'eg', 'eh',
              'er', 'es', 'et'])

worldmap.add('"F" Countries',
             ['fr', 'fi'])

worldmap.add('"P" Countries',
             ['pa', 'pe', 'pg', 'ph', 'pk',
              'pl', 'pr', 'ps', 'pt', 'py'])

worldmap.add('"Z" Countries',
             ['zm', 'zw'])

worldmap.add('"A" Countries',
             ['ad', 'ae', 'af', 'al', 'am', 'ao',
              'aq', 'ar', 'at', 'au', 'az'],
             color='black')

# save into the file
worldmap.render_to_file('abc.svg')

print("Success")