import matplotlib.pyplot as plt 
import numpy as np 

#class DataConteiner:
#
#
#    def __init__(self,x,y):
#
#        self._x = x
#        self._y = y
#
#    def plot(self, ax=None,**kwargs):
#        if ax is None:
#            ax = plt.gca()
#        ax.plot(self._x,self._y, **kwargs)
#        ax.set_title('Plotted from Data class')
#        plt.xlabel('подпись графика')
#        plt.ylabel('объемы графа')
#        return ax
#
#
#data = DataConteiner([0,1,2,3],[0,0.2,0.5,0.3])
#data.plot()  
        
fig,ax = plt.subplots(figsize =(5,3), layout='constrained')
np.random.seed(19680801)
t = np.arange(200)
x = np.cumsum(np.random.randn(200))
y = np.cumsum(np.random.randn(200))
linesx = ax.plot(t,x,label='Random walk for x')
linesy = ax.plot(t,y,label='Random walk for y')


ax.set_xlabel('Time [s]')
ax.set_ylabel('Distance [km]')
ax.set_title('Random walk example')
ax.legend()