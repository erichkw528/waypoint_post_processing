import numpy as np
import math
import csv
file_path = './circle.csv'
center = [37.91325259125717, -122.33390022675559]
r, contents = 0.001, str(center[0]) + ',' + str(center[1]) + ','
dic = {}
c, points = 10, []
angle_inc = 2*math.pi / c
for n in range(c):
    a = n * angle_inc
    points.append([center[0] + r*np.cos(a), center[1] + r*np.sin(a)])

with open(file_path, 'w') as file:
    fieldnames = ['lat', 'lon']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for p in points:
        writer.writerow({"lat": p[0], "lon": p[1]})
