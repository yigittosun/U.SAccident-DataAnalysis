import pandas as pd
import matplotlib.pyplot as plt


DataDosyasi=pd.read_csv('C:/Users/gorke/anaconda3/US_Accidents_Dec19.csv')
DataDosyasi.head()

DataDosyasi['timestamp'] = pd.to_datetime(DataDosyasi['Weather_Timestamp'], errors='coerce')
DataDosyasi['Hour'] = DataDosyasi['timestamp'] .dt.hour
DataDosyasi['Minute'] = DataDosyasi['timestamp'] .dt.minute
hours = [hour for hour, df in DataDosyasi.groupby('Hour')]
plt.plot(hours, DataDosyasi.groupby(['Hour'])['ID'].count())
plt.xticks(hours)
plt.xlabel('Hour')
plt.ylabel('Numer of accidents')
plt.grid(True)
plt.show()
