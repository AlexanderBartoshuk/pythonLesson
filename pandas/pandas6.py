import pandas as pd 

titanic = pd.read_csv('titanic.csv')
titanic.head()
air = pd.read_csv('air.csv')

titanic.sort_values(by=['Pclass','Age'], ascending=False).head()    

air.head()

data = {'Имя': ['Alice', 'Bob','Charli','Дэвид'],
        'Возраст': [25, 30, 35, 40], 
        'Оценка': [85, 90, 95, 80]}
df = pd.DataFrame(data)


sorted_data = df.sort_values(by='Возраст', ascending=True)
print(sorted_data)

filterdf = df[df['Оценка'] >= 85]
print(filterdf)

