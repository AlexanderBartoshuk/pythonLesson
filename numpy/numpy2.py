# Формулы
import pandas as pd
import numpy as np
import time 

#numpy_arr = np.arange(1000000, dtype=np.float64)
#start_time = time.time()
#np_result = np.sum(numpy_arr**2 + numpy_arr**3 + numpy_arr**4)
#end_time = time.time()
#print(f'Numpy takes {end_time-start_time:.6f} seconds ')
#print(np_result)
#
#
#taxi = np.genfromtxt('nyc_taxis.csv', delimiter=',')[1:]
#pickup_month = taxi[:, 1]
#
#january_bool = pickup_month == 1
#january = pickup_month[january_bool]
#january_rides = january.shape[0]
#print(january_rides)
#
#
#tip_amount = taxi[:, 12]
#total_fare = taxi[:, 13]
#high_tip_low_fare_bool = (tip_amount > 20) & (total_fare < 50)
#big_tip_rides = taxi[high_tip_low_fare_bool]
#print(big_tip_rides)
#

f500 = pd.read_csv('f500.csv', index_col=0)
f500.index.name = None

revenues = f500['revenues']
print(type(revenues))
print(revenues.head())

print(f500.info())
print(f500.describe())
print(f500['profit_change'].describe())

rank_change = f500['previous_rank'] - f500['rank']
print(rank_change.head())

print(f500['profits'].mean()) # средняя прибыль всех производителей
print(f500['profits'].max()) # максимальная прибыль для всех производителей
print(f500['profits'].min()) # мин. profit для всех производителей









