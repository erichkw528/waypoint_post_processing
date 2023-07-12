# ROAR Waypoint Post Processing

This repo contains two post processing scripts for the waypoint 
following project.

## Bag To CSV

This is a ROS node that connects to the /gps/fix topic and outputs
a csv file, named data.csv, in the current directory with latitude
and longitude data.

### Usage

Make sure the ros bag you want to collect data from is running:

`ros2 bag play [ros_bag_name]`

Then call

`python3 bag_to_csv.py`

and let the script run until the bag is finished. Afterwards,
you should find the data.csv file in your current directory.


## Map Visualizer

This is python script that takes in a csv file with latitude and
longitude data and visualizes it with google maps.

### Usage

In order to use this script, you will need a Google Maps API Key.
This can be set up [here](https://developers.google.com/maps/documentation/embed/get-api-key).

Afterwards, add this line to your ~/.bashrc

`export GOOGLE_API_KEY=<your_key>`

and either open a new terminal or run:

`source ~/.bashrc`

Then you should be able to run the script with:

`python3 map.py [path to csv file]`

and the map should be opened in your default browser. 
The zoom can be adjusted with the optional argument:

`python3 map.py [path to csv file] [zoom level (default is 15)]`

The circle.csv file is included and can be ran as an example using:

`python3 map.py circle.csv`


## Dists

This is a directory includes two scripts. 

dists_between.py expects to be given two csv files with latitude
and longitude coordinates will output maximum, minimum, mean,
and standard devation of distances between each coordinate.
This assumes both files have the same number of coordinates, 
if one file has more coordinates than the other, they will be ignored.

granularity.py expects to be given a single csv file with latitude and longitude
coordinates. It will output the same statistics as dists_between, but for the distance
between the current coordinate and the next coordinate.

### Usage

These scripts require geopy

`pip install geopy`

Then for granularity.py call

`python3 granularity.py <path to csv file>`

granularity.py will write a text file with the statistics that are printed out by default.

for dists_between.py call

`python3 dists_between.py <path to csv file> <path to csv file>`

This script takes a long time to run, so the percentage of how much it has run will be printed out.
This script currently samples only 100 points from the smaller track in order to find 
