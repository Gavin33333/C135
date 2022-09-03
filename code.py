import csv
from re import A 
import pandas as pd
import matplotlib.pyplot as plt

rows=[]
with open("Project135/data.csv") as f:
    a = csv.reader(f)
    for i in a:
        rows.append(i)

headers=rows[0]

df = pd.read_csv("Project135/data.csv")

star_name = df["Star Name"].tolist()
star_name.pop(0)


mass = df["Mass"].tolist()
mass.pop(0)


radius = df["Radius"].tolist()
radius.pop(0)


distance = df["Distance"].tolist()
distance.pop(0)


gravity = df["Gravity"].tolist()
gravity.pop(0)


plt.figure(figsize=(10,5))
plt.title("Stars vs Mass")
plt.xlabel("Name")
plt.ylabel("Mass")
plt.bar(star_name[0:9], mass[0:9])


plt.figure(figsize=(10,5))
plt.title("Stars vs Radius")
plt.xlabel("Name")
plt.ylabel("Radius")
plt.bar(star_name[0:9], radius[0:9])


plt.figure(figsize=(10,5))
plt.title("Stars vs Gravity")
plt.xlabel("Name")
plt.ylabel("Gravity")
plt.bar(star_name[0:9], gravity[0:9])


plt.figure(figsize=(10,5))
plt.title("Stars vs Distance")
plt.xlabel("Name")
plt.ylabel("Distance")
plt.bar(star_name[0:9], distance[0:9])


plt.show()



