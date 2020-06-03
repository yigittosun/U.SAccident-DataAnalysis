
import pandas as pd
import matplotlib.pyplot as plt

DataDosyasi=pd.read_csv('C:/Users/gorke/anaconda3/US_Accidents_Dec19.csv')
DataDosyasi.head()

baslangic = pd.to_datetime(DataDosyasi.Start_Time, format='%Y-%m-%d %H:%M:%S')
bitis = pd.to_datetime(DataDosyasi.End_Time, format='%Y-%m-%d %H:%M:%S')
fark = (bitis-baslangic)
en10 = fark.astype('timedelta64[m]').value_counts().nlargest(10)
print('En uzun 10 kaza'.format(en10.sum()*100/len(fark)))
(en10/en10.sum()).plot.bar(figsize=(8,8))
plt.title('Accident long')
plt.xlabel('Minute')
plt.ylabel('Rate');
