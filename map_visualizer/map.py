import bokeh
import pandas as pd
import sys
from bokeh.io import show
from bokeh.plotting import gmap
from bokeh.models import GMapOptions
from bokeh.models import ColumnDataSource
import os

api_key = os.environ['GOOGLE_API_KEY']
if len(sys.argv) < 2:
    print('need a csv file as an argument')
    sys.exit(1)

zoom = 15
if len(sys.argv) > 2:
    zoom = sys.argv[2]

file_path = sys.argv[1]
df = pd.read_csv(file_path, delimiter=',')


def plot(lat, lng, zoom=15, map_type='satellite'):
    bokeh_width, bokeh_height = 500, 400
    gmap_options = GMapOptions(lat=lat, lng=lng,
                               map_type=map_type, zoom=zoom)
    source = ColumnDataSource(df)
    p = gmap(api_key, gmap_options, title='Pays de Gex',
             width=bokeh_width, height=bokeh_height)
    center = p.circle('lon', 'lat', size=4, alpha=1,
                      color='red', source=source)
    show(p)
    return p


points = []
for i in range(len(df['lat'][:])):
    points.append([df['lat'][i], df['lon'][i]])
n = len(points)
center = [sum(df['lat']) / n, sum(df['lon']) / n]

p = plot(center[0], center[1], zoom=int(zoom))


# mapp = folium.Map(location=center, zoom_start=20, attr='Ersi')
# for p in points:
# folium.CircleMarker(p, radius=1, color='red', fill=True).add_to(mapp)
# mapp.show_in_browser()
