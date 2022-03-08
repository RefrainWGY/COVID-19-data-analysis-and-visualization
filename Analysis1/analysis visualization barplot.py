import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdate

from matplotlib import pyplot
from matplotlib.font_manager import FontProperties
font_set = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=15)

pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 500)

data = pd.read_csv("../data/covid_19_data.csv")


data_usa = data[(data["Country/Region"]== "US") & (data["ObservationDate"]== "01/19/2021") ]

newindex = data_usa['Deaths'].sort_values(ascending=True).index
data_usa_sorted = data_usa.reindex(newindex)

f,ax = plt.subplots(figsize=(18, 13))
sns.barplot(data = data_usa_sorted, x= 'Province/State', y = 'Deaths', palette = 'Blues')
plt.xticks(rotation=90)
plt.xlabel('州',fontproperties=font_set)
plt.ylabel('死亡人数',fontproperties=font_set)
plt.show()

data_china = data[(data["Country/Region"]== "Mainland China") & (data["ObservationDate"]== "01/19/2021") ]

f,ax = plt.subplots(figsize=(13, 13))
sns.barplot(data = data_china, y= 'Province/State', x = 'Confirmed', color = "yellow",label = "Confirmed")
sns.barplot(data = data_china, y= 'Province/State', x = 'Recovered',  color = "green",label = "Recovered")
ax.legend(loc='upper right',frameon = True)
plt.xlabel('')
plt.ylabel('城市',fontproperties=font_set)

plt.show()