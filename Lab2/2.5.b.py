import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# df1 = pd.read_csv("winequality-red_miss - Copy.csv")
df2 = pd.read_csv("landslide_data2_original.csv").drop(['dates', 'stationid'], axis=1)
df3 = pd.read_csv("landslide_data2_miss.csv").drop(['dates', 'stationid'], axis=1)

df3 = df3.fillna(method='ffill')

m1 = df3.mean()
m1 = m1.rename("mean_changed")
m2 = df2.mean()
m2 = m2.rename("mean_original")
m = pd.concat([m1, m2], axis=1, sort=False)
print(m)

# mo1 = df3.mode()
# mo1 = mo1.rename("mode_changed")
# mo2 = df2.mode()
# mo2 = mo2.rename("mode_original")
# mo = pd.concat([mo1, mo2], axis=1, sort=False)
# print(mo)

md1 = df3.median()
md1 = md1.rename("median_changed")
md2 = df2.median()
md2 = md2.rename("median_original")
md = pd.concat([md1, md2], axis=1, sort=False)
print(md)

sd1 = df3.std()
sd1 = sd1.rename("std_changed")
sd2 = df2.std()
sd2 = sd2.rename("std_original")
sd = pd.concat([sd1, sd2], axis=1, sort=False)
print(sd)

for i in df3.columns:
    plt.boxplot([df3[i], df2[i]])
    plt.title(i)
    # plt.boxplot(df3[i])
    # plt.boxplot(df2[i])
    # plt.show()
# print(df1)


RMSE = ((df3-df2)**2).mean()**.5
print("*********RMSE**********")
print(RMSE)

