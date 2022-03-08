import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdate

plt.savefig("save.png", dpi=300, bbox_inches="tight")

pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 500)

data = pd.read_csv("../data/covid_19_data.csv")

data_corre = data.drop("SNo", axis = 1)



corre1 = data_corre.corr(method ='pearson')
corre2 = data_corre.corr(method ='kendall')
corre3 = data_corre.corr(method ='spearman')


print("Standard Correlation Coefficients")
print(corre1)
print("-------------------------------------")
print("Kendall Tau Correlation Coefficients")
print(corre2)
print("-------------------------------------")
print("Spearman Rank Correlation Coefficients")
print(corre3)

f,ax = plt.subplots(figsize=(15, 13))  
sns.heatmap(corre1, annot= True, fmt= '.2f',cmap="summer")
plt.tight_layout()
plt.show()

for a in data.columns:

    list1 = list(data[a])
    count = 0

    for i in list1:
        if (i == "Recovered"):
            count = count + 1
        else:
            count = count

    print(" The number of ""'Recovered'"" value inside {} column is {}".format(a, count))
