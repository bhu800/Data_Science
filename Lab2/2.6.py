import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df1 = pd.read_csv("landslide_data2_miss - Copy.csv")
df2 = pd.read_csv("landslide_data2_original.csv").drop(['dates', 'stationid'], axis=1)
df3 = pd.read_csv("landslide_data2_miss.csv").drop(['dates', 'stationid'], axis=1)

df_t = df3['temperature']

df4 = df_t.fillna(0)
plt.hist(df4)
plt.show()

df5 = df_t.fillna(df_t.median())
plt.hist(df5)
plt.show()

df6 = df_t.interpolate()
plt.hist(df6)
plt.show()

grouped = df1.groupby(['stationid'])

for name, group in grouped:
    # print(name)
    # print(group)
    plt.plot(group['dates'], group['temperature'])
    plt.title(name)
    plt.show()

