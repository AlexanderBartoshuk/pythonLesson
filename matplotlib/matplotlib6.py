import matplotlib.pyplot as plt 
import numpy as np 

#fig = plt.figure(figsize=(4,2), facecolor='r', layout='constrained')
#fig.suptitle('A nice Matplotlib figure')
#ax = fig.add_subplot()
#ax.set_title('Alex', loc='left', fontstyle='oblique', fontsize='medium')



plt.subplot(1,2,1)
plt.plot([1,2,3],[0,0.5,0.2])

plt.subplot(1,2,2)
plt.plot([3,2,1],[0,0.5,0.2])

plt.suptitle('Мои диаграммы в Matplotlib')
plt.gcf().set_facecolor('green')


for i in range(1,3):
    plt.subplot(1,2,i)
    plt.xlabel('МОЁ')


