import pandas as pd
import matplotlib.pyplot as plt

DataDosyasi=pd.read_csv('C:/Users/gorke/anaconda3/US_Accidents_Dec19.csv')
DataDosyasi.head()

sehirler = DataDosyasi["City"].value_counts().head(50)
fig,ax = plt.subplots(figsize = (18,5))
ax.bar(x = sehirler.index, height=sehirler)
ax.set_xticklabels(sehirler.index,rotation = 90)
plt.show()
