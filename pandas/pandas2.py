import pandas as pd

titanic = pd.read_csv('titanic.csv')

titanic.head(8)

titanic.dtypes

ages = titanic['Age']
ages.head()
titanic['Age'].shape

age_sex = titanic[['Age','Sex']]
age_sex.head()
titanic[['Age','Sex']].shape

above_35 = titanic[titanic['Age'] > 35]
above_35.head()
titanic['Age'] > 35

class_23 = titanic[titanic['Pclass'].isin([2,3])]
class_23.head()
class_23 = titanic[(titanic['Pclass']==2) | (titanic['Pclass'] == 3)]
class_23.head()


adult_names = titanic.loc[titanic['Age'] > 35, 'Name']
adult_names.head()

titanic.iloc[9:25, 2:5]

