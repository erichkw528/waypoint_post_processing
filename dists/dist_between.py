import pandas as pd
import sys
import os
import geopy.distance
import statistics as st


def d(p1, p2):
    return geopy.distance.geodesic(p1, p2).m


def gradient_descent(track, p, i):

    return closest_point


if len(sys.argv) < 3:
    print('need two csv files as an argument')
    sys.exit(1)

file_path1 = sys.argv[1]
file_path2 = sys.argv[2]
df1 = pd.read_csv(file_path1, delimiter=',')
df2 = pd.read_csv(file_path2, delimiter=',')

points1, points2 = [], []
for i in range(len(df1['lat'][:])):
    points1.append([df1['lat'][i], df1['lon'][i]])
for i in range(len(df2['lat'][:])):
    points2.append([df2['lat'][i], df2['lon'][i]])

n, m = len(points1), len(points2)

dists = [0] * max(n, m)
c = 1000  # number of points that will be check for spatially closest_point

if n >= m:
    for i in range(n):
        # print(str(100 * (i / n)) + " % done")
        closest_point, its_distance = [-1, -1], float("inf")
        for j in range((i - int(c/2)) % m, (i + int(c/2)) % m):
            dis = d(points1[i], points2[j])
            if dis < its_distance:
                closest_point = points2[j]
                its_distance = dis
        dists[i] = its_distance
else:
    for i in range(m):
        print(str(100 * (i / m)) + " % done")
        closest_point, its_distance = [-1, -1], float("inf")
        strt, end = min((i - int(c/2)) % n, (i + int(c/2)) %
                        n), max((i - int(c/2)) % n, (i + int(c/2)) % n)
        for j in range(strt, end):
            dis = d(points2[i], points1[j])
            if dis < its_distance:
                closest_point = points2[j]
                its_distance = dis
        dists[i] = its_distance

out = "Max Distance: " + str(max(dists)) + "\n"
out += "Min Distance: " + str(min(dists)) + "\n"
out += "Mean Distance: " + str(st.mean(dists)) + "\n"
# out += "Standard Deviation: " + str(st.stdev(dists)) + "\n"

print(out)

if len(sys.argv) > 3:
    f = open(file_path1[:-3] + "_vs_" + file_path2[:-3] + "txt", "a")
    f.write(out)
    f.close()
