import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdate

from matplotlib import pyplot
from matplotlib.font_manager import FontProperties

font_set = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=15)

data = pd.read_csv('../data/covid_19_data.csv')
print(data.head())


data.isnull().sum()[data.isnull().sum()>0]
data = data.drop(columns=['Province/State','SNo','Last Update'])
data.isnull().sum()[data.isnull().sum()>0]
name = ["('St. Martin',)", 'Bahamas, The', 'The Bahamas', 'Congo (Brazzaville)', 'The Gambia', 'Gambia, The',
       'Cabo Verde','Mainland China', 'UK','Ireland']
replace=['St. Martin', 'Bahamas', 'Bahamas', 'Republic of the Congo', 'Gambia', 'Gambia', 'Cape Verde',
         'China', 'United Kingdom', 'Republic of Ireland']


data.replace(to_replace=name, value=replace, inplace=True)
data['ObservationDate'] = pd.to_datetime(data['ObservationDate'])
data["ActiveConfirmed"] = data.Confirmed - data.Recovered - data.Deaths
start = data.ObservationDate.min()
end = data.ObservationDate.max()
report = data[data.ObservationDate == end]
daily_cummulative = report.groupby('Country/Region')[['Confirmed','Deaths']].agg('sum')
grouped_data = data.groupby(['ObservationDate','Country/Region'])[['Confirmed','Recovered','Deaths','ActiveConfirmed']].agg('sum').reset_index()
grouped_data.tail()
plt.figure(figsize=(15,9))
sns.lineplot(x='ObservationDate', y='Confirmed', hue='Country/Region',
                data=grouped_data[grouped_data['Country/Region'].isin(['US','India','Brazil',
                                                                       'Russia','United Kingdom'])])
plt.xlabel('观察日期',fontproperties=font_set)
plt.ylabel('确诊人数',fontproperties=font_set)
plt.title('受2019冠状病毒感染最严重的国家',fontproperties=font_set)
plt.show()

plt.figure(figsize=(15,9))
sns.lineplot(x='ObservationDate', y='Deaths', hue='Country/Region',
                data=grouped_data[grouped_data['Country/Region'].isin(['US','India','Brazil',
                                                                       'Mexico','United Kingdom'])])
plt.xlabel('观察日期',fontproperties=font_set)
plt.ylabel('死亡人数',fontproperties=font_set)
plt.title('新冠肺炎死亡人数最多的国家',fontproperties=font_set)
plt.show()

daily_cummulative.Confirmed.sort_values(ascending=False)[:20].plot(kind='bar',figsize=(15,6))
plt.title(f'受新冠肺炎影响最大的20个国家{end}',fontproperties=font_set)
plt.ylabel('确诊人数',fontproperties=font_set)
plt.show()

daily_cummulative.Deaths.sort_values(ascending=False)[:20].plot(kind='bar',figsize=(15,6))
plt.title(f'受新冠肺炎伤害最大的20个国家{end}',fontproperties=font_set)
plt.ylabel('死亡人数',fontproperties=font_set)
plt.show()

