
import pandas as pd
import matplotlib.pyplot as plt


DataDosyasi=pd.read_csv('C:/Users/gorke/anaconda3/US_Accidents_Dec19.csv')
DataDosyasi.head()

fig, ax=plt.subplots(figsize=(16,7))
DataDosyasi['Visibility(mi)'].value_counts().sort_values(ascending=False).head(8).plot.bar(width=0.5,edgecolor='k',align='center',linewidth=2)
plt.xlabel('Visibilty(mil)',fontsize=20)
plt.ylabel('Accident count',fontsize=20)
ax.tick_params(labelsize=20)
plt.title('Visibility Amount Per Mile Top 5',fontsize=25)
plt.grid()
plt.ioff()
