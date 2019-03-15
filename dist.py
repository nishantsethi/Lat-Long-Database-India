# Gives a database with distaces provided a csv with latitude and longitude

from math import sin, cos, sqrt, atan2, radians
import pandas as pd
from tqdm import tqdm

df = pd.read_csv("updated_city.csv")
R = 6373.0
lat = df.lat
longi = df.long
name = df.s


for i in tqdm(range(len(lat))):
    lat[i] = radians(float(lat[i]))
    longi[i] = radians(float(longi[i]))
# print(lat)
# print(longi)
dist = []
for i in tqdm(range(len(lat))):
    d = []
    for j in range(len(lat)):
        a = sin((lat[i]-lat[j]) / 2)**2 + cos(lat[i]) * \
            cos(lat[j]) * sin((longi[i]-longi[j]) / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        d.append(float(R * c))
    dist.append(d)

# print(dist)

ddf = pd.DataFrame(dist, index=name, columns=name)
print(ddf)
ddf.to_csv('dist.csv')
