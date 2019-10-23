import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df1 = pd.read_csv("landslide_data2_miss - Copy.csv")
df2 = pd.read_csv("landslide_data2_original.csv").drop(['dates', 'stationid'], axis=1)
df3 = pd.read_csv("landslide_data2_miss.csv").drop(['dates', 'stationid'], axis=1)

# 1
nan_row = df1.isna().sum(axis=1)
# print(nan_row)
# *****
nan_row1 = df1.isna().sum(axis=0)
print(nan_row1)
# ****
val_cnt = nan_row.value_counts().sort_index()
print(val_cnt)
cnt = val_cnt.values
vals = val_cnt.index.values
# print(vals, cnt)
plt.plot(vals, cnt)
plt.show()

# 2
print(val_cnt[3:])

# 3

# (a)
print(len(df1))
df1 = df1.drop(df1.index[nan_row >= 4]) #-->M1
print(len(df1))

# # M2
# print(len(df1))
# df1 = df1.dropna(thresh=5, axis=0) # thresh = at least this many non-NaN values are required
# print(len(df1))

# (b)
print(len(df1))
# print(np.isfinite(df1["stationid"].str.len()))
df1 = df1[np.isfinite(df1["stationid"].str.len())]
print(len(df1))
# #
# # 4
nan = df1.isna().sum()
print(nan)
total_nan = nan.sum()
print(total_nan)

