import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdate

pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 500)

data = pd.read_csv("../data/covid_19_data.csv")

data_turkey = data[data["Country/Region"]== "Turkey"]

f,ax = plt.subplots(figsize=(15, 10))
plt.plot(data_turkey['ObservationDate'],data_turkey['Confirmed'], label = "Confirmed Covid-19",color = "#cc0000")
plt.plot(data_turkey['ObservationDate'],data_turkey['Recovered'], label = "Recovered Covid-19", color ="#330033",linestyle = 'dotted')
locator = mdate.MonthLocator()
plt.gca().xaxis.set_major_locator(locator)
plt.legend(loc='upper left')
plt.xlabel('time')
plt.ylabel('value * 10^6,')   
plt.title('Confirmed and Recovered Covid-19 values for months')
plt.show()
