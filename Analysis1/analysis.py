import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdate

pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 500)

data = pd.read_csv("../data/covid_19_data.csv")

print(data.head(3))
print("-------------------------------------------------------------------------")
print("-------------------------------------------------------------------------")
print(data.info(null_counts = False))
print("-------------------------------------------------------------------------")
print("-------------------------------------------------------------------------")
print(data.columns)  
print("-------------------------------------------------------------------------")
print("-------------------------------------------------------------------------")
print(data.describe())

print(data["Country/Region"].unique())

say = data["Country/Region"].unique()
count = 0

for i in say:
    count = count + 1
print("Number of different Country/Region:",count)
