import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("winequality-red.csv", sep=";")
# print(df)
'''
# 1
mean = df.mean()
print(mean)
median = df.median()
print(median)
mode = df.mode()
print(mode)
max = df.max()
print(max)
min = df.min()
print(min)
std = df.std()
print(std)

# print(df.columns[0])

# 2
for i in range(len(df.columns)-1):
    plt.scatter(df["quality"], df.iloc[:, i])
    plt.xlabel("quality")
    plt.ylabel(df.columns[i])
    plt.show()

per_corr = df.corr()
print(per_corr)

for i in range(len(df.columns)):
    plt.hist(df.iloc[:, i])
    plt.ylabel("frequency")
    plt.xlabel(df.columns[i])
    plt.show()
'''
df_grp_quality = df.groupby(['quality'])["pH"]

for name, group in df_grp_quality:
    plt.hist(group)
    plt.ylabel("frequency")
    plt.xlabel("pH")
    print(name)
    plt.title("quality : {}".format(name))
    plt.show()

# 6
for i in df.columns:
    plt.boxplot(df[i])
    plt.show()
