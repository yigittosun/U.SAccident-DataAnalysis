
import pandas as pd
import matplotlib.pyplot as plt

DataDosyasi=pd.read_csv('C:/Users/gorke/anaconda3/US_Accidents_Dec19.csv')
DataDosyasi.head()
fig, ax=plt.subplots(figsize=(16,7))
DataDosyasi['Weather_Condition'].value_counts().sort_values(ascending=False).head(10).plot.bar(width=0.5,edgecolor='k',align='center',linewidth=2)
plt.xlabel('Weather',fontsize=20)
plt.ylabel('Accident count',fontsize=20)
ax.tick_params(labelsize=20)
plt.title('Weather conditions for accidents',fontsize=25)
plt.grid()
plt.ioff()
