import pandas as pd

import matplotlib.pyplot as plt 

air_quality = pd.read_csv('air.csv')

air_quality.head()

air_quality.plot()
plt.show()

air_quality['station_paris'].plot()
plt.show()

air_quality.plot.scatter(x='station_london',y='station_paris', alpha = 0.5)
# scatter - это точечный график 
plt.show()

[
    method_name 
    for method_name in dir(air_quality.plot)
    if not method_name.startswith('_') # startswith - возвращает если строка начинается с указанного символа    
]

axs = air_quality.plot.area(figsize=(12,4), subplots=True)
plt.show()

fig, axs = plt.subplots(figsize=(12,4))

air_quality.plot.area(ax=axs)

axs.set_ylabel('NO$_2$ concentration')
fig.savefig('no2_concentrations.png')  # Save the Figure/Axes using the existing Matplotlib method.
plt.show()


