import matplotlib.pyplot as plt
import numpy as np

lat = []
lon = []

with open("/Users/hrishikeshhpillai/Hrishi/hrishikeshhpillai/GNSSToolkit/Rinex/data/iisc0320.pos") as f:
    next(f)
    for line in f:
        values = line.split()
        lat.append(float(values[2]))
        lon.append(float(values[3]))

plt.scatter(lon, lat, c='blue', s=10)
plt.title("Latitude vs Longitude")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()

