import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

pd.set_option('display.max_rows', 200)
pd.set_option('display.max_columns', 200)
plt.style.use('ggplot')


df=pd.read_csv('C:/Users/gorke/anaconda3/US_Accidents_Dec19.csv')


df['Start_Time'] = pd.to_datetime(df['Start_Time'], errors='coerce')
df['End_Time'] = pd.to_datetime(df['End_Time'], errors='coerce')

df['Year']=df['Start_Time'].dt.year
df['Month']=df['Start_Time'].dt.strftime('%b')
df['Day']=df['Start_Time'].dt.day
df['Hour']=df['Start_Time'].dt.hour
df['Weekday']=df['Start_Time'].dt.strftime('%a')


td='Time_Duration(min)'
df[td]=round((df['End_Time']-df['Start_Time'])/np.timedelta64(1,'m'))




feature_lst=['Source','TMC','Severity','Start_Lng','Start_Lat','Distance(mi)','Side','City','County','State','Timezone','Temperature(F)','Humidity(%)','Pressure(in)', 'Visibility(mi)', 'Wind_Direction','Weather_Condition','Amenity','Bump','Crossing','Give_Way','Junction','No_Exit','Railway','Roundabout','Station','Stop','Traffic_Calming','Traffic_Signal','Turning_Loop','Sunrise_Sunset','Hour','Weekday', 'Time_Duration(min)']

df_sel=df[feature_lst].copy()


df_sel.isnull().mean()
df_sel.dropna(subset=df_sel.columns[df_sel.isnull().mean()!=0], how='any', axis=0, inplace=True)
df_sel.shape




state='TX'


df_state=df_sel.loc[df_sel.State==state].copy()
df_state.drop('State',axis=1, inplace=True)



df_state_dummy = pd.get_dummies(df_state,drop_first=True)


df=df_state_dummy



target='Severity'


y = df[target]
X = df.drop(target, axis=1)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=21, stratify=y)

algo_lst=['Logistic Regression',' K-Nearest Neighbors','Decision Trees','Random Forest']


accuracy_lst=[]


lr = LogisticRegression(random_state=0)
lr.fit(X_train,y_train)
y_pred=lr.predict(X_test)


acc=accuracy_score(y_test, y_pred)


accuracy_lst.append(acc)

print("Accuracy_score of Logistic regression algorithm {:.3f}.".format(acc))


knn = KNeighborsClassifier(n_neighbors=6)


knn.fit(X_train,y_train)


y_pred = knn.predict(X_test)


acc=accuracy_score(y_test, y_pred)

accuracy_lst.append(acc)

print('Knn.score of K-Nearest Neighbors algorithm is {:.3f}.'.format(knn.score(X_test, y_test)))
print('Accuracy_score of K-Nearest Neighbors algorithm is {:.3f}.'.format(acc))





dt_entropy = DecisionTreeClassifier(max_depth=8, criterion='entropy', random_state=1)



dt_entropy.fit(X_train, y_train)


y_pred= dt_entropy.predict(X_test)


accuracy_entropy = accuracy_score(y_test, y_pred)


print('Accuracy score of Decision Tree algorithm for entropy is {:.3f}.'.format(accuracy_entropy))




dt_gini = DecisionTreeClassifier(max_depth=8, criterion='gini', random_state=1)



dt_gini.fit(X_train, y_train)


y_pred= dt_gini.predict(X_test)


accuracy_gini = accuracy_score(y_test, y_pred)

acc=accuracy_gini
accuracy_lst.append(acc)


print('Accuracy score of Decision Tree algorithm for gini is {:.3f}.'.format(accuracy_gini))




clf=RandomForestClassifier(n_estimators=100)


clf.fit(X_train,y_train)

y_pred=clf.predict(X_test)


acc=accuracy_score(y_test, y_pred)


accuracy_lst.append(acc)


print("Accuracy score for Randon forest algorithm is {:.3f}.".format(acc))



y_ticks=np.arange(len(algo_lst))

df_acc=pd.DataFrame(list(zip(algo_lst, accuracy_lst)), columns=['Algorithm','Accuracy_Score']).sort_values(by=['Accuracy_Score'],ascending = True)


ax=df_acc.plot.barh('Algorithm', 'Accuracy_Score', align='center',legend=False,color='0.5')


for i in ax.patches:
    
    ax.text(i.get_width()+0.02, i.get_y()+0.2, str(round(i.get_width(),2)), fontsize=10)


plt.xlim(0,1.05)
plt.xlabel('Accuracy Score')
plt.yticks(y_ticks, df_acc['Algorithm'], rotation=0)
plt.title('Algorithm predicting score of severity in Texas'.format(state))

plt.show()