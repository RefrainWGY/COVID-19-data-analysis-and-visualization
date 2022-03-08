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

data_usa = data[(data["Country/Region"]== "US") & (data["ObservationDate"]== "01/19/2021")]

data_china = data[(data["Country/Region"]== "Mainland China") & (data["ObservationDate"]== "01/19/2021") ]

data_combined_usa_china = data_usa.append(data_china)
data_combined_usa_china2 = pd.concat([data_usa,data_china],axis = 0 )

data_combined_usa_china["color"] = [ "blue" if i == "US" else "red" for i in data_combined_usa_china["Country/Region"]]
data_combined_usa_china2["color"] = [ "blue" if i == "US" else "red" for i in data_combined_usa_china["Country/Region"]]


print(pd.concat([data_combined_usa_china.head(3),data_combined_usa_china.tail(3)],axis = 0))

f,ax = plt.subplots(figsize=(20, 10))
plt.bar(data_combined_usa_china["Province/State"],data_combined_usa_china["Confirmed"], color = data_combined_usa_china.color)
plt.ylabel('确诊病例',fontproperties=font_set)
plt.xticks(rotation=90)
plt.title("条形图",fontproperties=font_set)
plt.show()



# f,ax = plt.subplots(figsize=(20, 10))
# plt.bar(data_combined_usa_china2["Province/State"],data_combined_usa_china2["Confirmed"],color = data_combined_usa_china2["color"])
# plt.ylabel('Confirmed Cases')
# plt.xticks(rotation=90)
# plt.title("Bar Plot of combined data by concatenating")
# plt.show()