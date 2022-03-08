import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdate

from matplotlib import pyplot
from matplotlib.font_manager import FontProperties
font_set = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=15)
# pd.set_option('display.max_columns', 100)
# pd.set_option('display.width', 500)

data = pd.read_csv("../data/covid_19_data.csv")

data_usa = data[(data["Country/Region"]== "US") & (data["ObservationDate"]== "01/19/2021")]

data_china = data[(data["Country/Region"]== "Mainland China") & (data["ObservationDate"]== "01/19/2021") ]

data2 = pd.read_csv("../data/time_series_covid_19_confirmed.csv")
print(data2.head(20))

a = data2.groupby("Country/Region").sum()
last_announcements = a.iloc[:,[-1]]
last_announcements.rename(columns={'{}'.format(last_announcements.columns[0]) : "Confirmed"},inplace=True)
print(last_announcements)

countries = ["US", "Turkey", "China"]

for i in last_announcements.index:
    if i in countries:
        continue
    else:
        last_announcements.drop(last_announcements.index[last_announcements.index == i], inplace=True)

print(last_announcements)

labels = last_announcements.index
f,ax = plt.subplots(figsize=(13, 13))
plt.pie(last_announcements["Confirmed"], labels= labels ,explode=(0.15,0.1,0.1),autopct='%1.1f%%' )
plt.title("三个国家中确诊的新冠肺炎人数比例",fontproperties=font_set)
plt.legend()
plt.show()