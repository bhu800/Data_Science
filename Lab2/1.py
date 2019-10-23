import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df1 = pd.read_csv("winequality-red_miss - Copy.csv")
df2 = pd.read_csv("winequality-red_original.csv", sep=";")
df3 = pd.read_csv("winequality-red_miss.csv")
# print(df2)

# # A
# # 1, 2
# nan = df1.isna().sum()
# print(nan)
#
# # 3
# df1 = df1.replace('na', np.NaN)
# print(df1)
# nan = df1.isna().sum()
# print(nan)
# # print(len(df1.iloc[0, 0]))
#
# # B
# # 1
# nan_row = df1.isna().sum(axis=1)
# print(nan_row)
# val_cnt = nan_row.value_counts().sort_index()[1:]
# print(val_cnt)
# cnt = val_cnt.values
# vals = val_cnt.index.values
# print(vals, cnt)
# plt.plot(vals, cnt)
# plt.show()
#
# # 2
# print(val_cnt[5:])
#
# # 3
# # (a)
# # df1 = df1.drop(df1.index[nan_row >= 5]) #-->M1
# # print(len(df1))
# # M2
# df1 = df1.dropna(thresh=8, axis=0) # thresh = at least this many non-NaN values are required
# print(len(df1))
# # (b)
# df1 = df1[np.isfinite(df1["quality"])]
# print(len(df1))
#
# # 4
# nan = df1.isna().sum()
# print(nan)
# total_nan = nan.sum()
# print(total_nan)







