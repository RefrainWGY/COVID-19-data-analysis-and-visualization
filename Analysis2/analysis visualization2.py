import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdate

from matplotlib import pyplot
from matplotlib.font_manager import FontProperties
font_set = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=15)

data = pd.read_csv('../data/covid_19_data.csv')

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




def beta(row):
    if row['Confirmed'] == 0:
        return 0
    else:
        return row['ActiveConfirmed']/row['Confirmed']

def gamma(row):
    if row['Confirmed'] == 0:
        return 0
    else:
        return row['Recovered']/row['Confirmed']

def delta(row):
    if row['Confirmed'] == 0:
        return 0
    else:
        return row['Deaths']/row['Confirmed']
grouped_data['beta'] = grouped_data.apply(beta, axis=1)
grouped_data['gamma'] = grouped_data.apply(gamma, axis=1)
grouped_data['delta'] = grouped_data.apply(delta, axis=1)
transDynamics = grouped_data[['ObservationDate','Country/Region','beta','gamma','delta']]
def infective_rate(row):
    return row['beta'] - row['gamma'] -row['delta']
transDynamics['infective_rate'] = transDynamics.apply(infective_rate, axis=1)
def decision(row):

    if row['beta'] > row['gamma']:


        if row['gamma'] >= row['delta']:
            return 'Hope'
        else:
            return 'Danger'


    if row['beta'] <= row['gamma']:


        if row['gamma'] >= row['delta']:
            return 'Good'
        else:
            return 'Apocalyse'

transDynamics['decision'] = transDynamics.apply(decision, axis=1)
plt.figure(figsize=(15,8))
sns.lineplot(x='ObservationDate', y='infective_rate',
             data=transDynamics[transDynamics['Country/Region'] == 'China'], hue='decision')
plt.xlabel('观察日期',fontproperties=font_set)
plt.ylabel('感染率',fontproperties=font_set)
plt.title('中国:流行病趋势',fontproperties=font_set)
plt.show()

plt.figure(figsize=(15,8))
china = transDynamics[transDynamics['Country/Region'] == 'China']
sns.countplot(china.decision)
plt.title('中国:流行病状况',fontproperties=font_set)
plt.xlabel('状况',fontproperties=font_set)
plt.ylabel('天数',fontproperties=font_set)
plt.show()