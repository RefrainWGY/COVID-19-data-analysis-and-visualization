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



f,ax = plt.subplots(figsize=(20, 10))
plt.bar(data_usa["Province/State"],data_usa["Confirmed"])
plt.xticks(rotation=90)  
plt.ylabel('确诊病例 (10^6)',fontproperties=font_set)
plt.show()


data_china = data[(data["Country/Region"]== "Mainland China") & (data["ObservationDate"]== "01/19/2021") ]

f,ax = plt.subplots(figsize=(20, 10))
plt.bar(data_china["Province/State"],data_china["Confirmed"])
plt.xticks(rotation=90)
plt.ylabel('确诊病例',fontproperties=font_set)
plt.show()


