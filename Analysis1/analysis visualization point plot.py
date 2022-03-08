import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdate


data = pd.read_csv("../data/covid_19_data.csv")

data_turkey2 = data[data["Country/Region"]== "Turkey"]
data_turkey2.drop("SNo", axis = 1, inplace = True)
date_list = [i for i in data_turkey2["ObservationDate"]]
datetime_object = pd.to_datetime(date_list)
data_turkey2["ObservationDate"] = datetime_object
data_turkey2.set_index("ObservationDate", inplace = True)
turkeyaylıkort = data_turkey2.resample("M").mean()


f,ax = plt.subplots(figsize=(18, 13))
sns.pointplot(x = turkeyaylıkort.index , y = turkeyaylıkort.Confirmed , markers = "X" , color = "red")
plt.xticks(rotation=45)
plt.show()