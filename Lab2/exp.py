import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df1 = pd.read_csv("winequality-red_miss - Copy.csv")
df2 = pd.read_csv("winequality-red_original.csv", sep=";")
# print(df2)

df1["fixed acidity"][0] = "ADADAS"
print(df1["fixed acidity"][0])
print(df1)