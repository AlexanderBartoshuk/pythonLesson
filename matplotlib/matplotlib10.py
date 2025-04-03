import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.units as minuts 


fig, ax = plt.subplots(figsize=(5.4,2), layout ='constrained')
time = np.arange('1980-01-01', '1980-06-25', dtype='datetime64[D]')
x = np.arange(len(time))
ax.plot(time,x)


fig, ax = plt.subplots(figsize=(5.4,2), layout ='constrained')
time = np.arange('1980-01-01', '1980-06-25', dtype='datetime64[D]')
x = np.arange(len(time))
ax.plot(time,x)
ax.plot(0,0,'d')
ax.text(0,0,'Float x=0', rotation=45)

fig, ax = plt.subplots(figsize=(5.4,2), layout ='constrained')
time = np.arange('1980-01-01', '1980-06-25', dtype='datetime64[D]')
x = np.arange(len(time))
ax.plot(time,x)
ax.xaxis.set_major_locator(mdates.MonthLocator(bymonth=np.arange(1,13,2)))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b'))
ax.set_xlabel('1980')



data = {'appple': 16, 'orange':15, 'lemon': 25, 'lime': 5}
names = list(data.keys())
values = list(data.values())


fig, axs = plt.subplots(1,3, figsize=(7,3), sharey=True, layout='constrained')
axs[0].bar(names, values) # diagram
axs[1].scatter(names, values) # points 
axs[2].plot(names, values) # lines
fig.suptitle('Categorical plotting')


