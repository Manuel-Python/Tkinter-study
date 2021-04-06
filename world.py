import pandas as pd
import plotly.express as px

# download dataset
#!wget
#https: // covid.ourworldindata.org / data / owid - covid - data.csv

# import dataset
df = pd.read_csv('owid-covid-data.csv')

# select entries with the continent as asia
df = df[df.continent == 'Asia']

# plot
fig = px.choropleth(df, locations="iso_code",
                    color="new_cases",
                    hover_name="location",
                    animation_frame="date",
                    title="Daily new COVID cases",
                    scope='asia', color_continuous_scale=px.colors.sequential.PuRd)

fig["layout"].pop("updatemenus")
fig.show()