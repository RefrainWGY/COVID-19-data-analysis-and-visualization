import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdate

pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 500)

data = pd.read_csv("../data/covid_19_data.csv")

filter1 = data["Province/State"] == "Recovered"
filtered_data = data[filter1]
print(filtered_data.head(20))

print(filtered_data["Country/Region"].unique())

datacleared = data[(data["Country/Region"] != "US") & (data["Country/Region"] != "Canada")]
data_correlation = datacleared.drop("SNo",axis=1)
print(data_correlation.corr())

datacleared2 = data[(data["Country/Region"] != "US") & (data["Country/Region"] != "Canada") & (data["Recovered"] != 0 ) ]
data_correlation2 = datacleared2.drop("SNo",axis=1)
print(data_correlation2.corr())