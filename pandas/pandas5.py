import pandas as pd 
import matplotlib.pyplot as plt

tit = pd.read_csv('titanic.csv')
tit.head()

tit['Age'].mean()
tit[['Age','Fare']].median()

tit.agg(
    {
        'Age': ['min','max','median','skew'],
        'Fare': ['min','max','median','skew']
    }
)

tit[['Sex','Age']].groupby('Sex').mean()

tit.groupby('Sex').mean(numeric_only=True)

tit['Pclass'].value_counts()

tit.groupby('Pclass')['Pclass'].count()
    