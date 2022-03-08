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

data_turkey = data[data["Country/Region"]== "Turkey"]

data_turkey.plot(kind = "scatter", x='Deaths',y='Confirmed',grid = True,color = "black", s = 10 ,figsize=(15,10))
plt.xlabel('死亡人数',fontproperties=font_set)
plt.ylabel('确诊人数',fontproperties=font_set)
plt.title('散点图',fontproperties=font_set)
plt.show()
f,ax = plt.subplots(figsize=(15, 10))
plt.scatter(data_turkey["Deaths"],data_turkey["Confirmed"],color = "red")
plt.grid()
plt.xlabel('死亡人数',fontproperties=font_set)
plt.ylabel('确诊人数',fontproperties=font_set)
plt.title('散点图',fontproperties=font_set)
plt.show()

data_greece = data[(data["Country/Region"]== "Greece") ]

data_greece.plot(kind = "scatter", x='Deaths',y='Confirmed',grid = True,color = "blue",figsize=(10,7),marker = "v")
plt.xlabel('死亡人数',fontproperties=font_set)
plt.ylabel('确诊人数',fontproperties=font_set)
plt.title('散点图',fontproperties=font_set)
plt.show()

data_bulgaria = data[(data["Country/Region"]== "Bulgaria") ]

data_bulgaria.plot(kind = "scatter", x='Deaths',y='Confirmed',grid = True,color = "green",figsize=(10,7),marker = "d",s = 40)
plt.xlabel('死亡人数',fontproperties=font_set)
plt.ylabel('确诊人数',fontproperties=font_set)
plt.title('散点图',fontproperties=font_set)
plt.show()

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

