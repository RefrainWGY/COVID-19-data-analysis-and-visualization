import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdate

pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 500)

data = pd.read_csv("../data/covid_19_data.csv")

data_usa = data[(data["Country/Region"]== "US") & (data["ObservationDate"]== "01/19/2021")]

data_china = data[(data["Country/Region"]== "Mainland China") & (data["ObservationDate"]== "01/19/2021") ]

x = [1,1,2,5,1,3,5,9,5,7,8,6,8,1,5,3,4,6,8,7,9,5,8]
print("we will have bar plot of x: {} ".format(x))

f,ax = plt.subplots(figsize=(20, 10))
plt.hist(x, bins = 50)
plt.show()