import numpy as np
import matplotlib.pyplot as plt 

import matplotlib.colors as mcolors 
import matplotlib.gridspec as gridspec

plt.rcParams['savefig.facecolor'] = '0.8'
plt.rcParams['figure.figsize'] = 4.5,4
plt.rcParams['figure.max_open_warning'] = 50

def example_plot(ax, fontsize=12, hide_labels= False):
    ax.plot([1,2])

    ax.locator_params(nbins=3)
    if hide_labels:
        ax.set_xticklabels([])
        ax.set_yticklabels([])
    
    else:
        ax.set_xlabel('x-label', fontsize=fontsize)
        ax.set_ylabel('y-label', fontsize=fontsize)
        ax.set_title('Title', fontsize=fontsize)

fig,axs = plt.subplots(2,2,layout='constrained')
for ax in axs.flat:
    example_plot(ax, fontsize=24)




fig, axs = plt.subplots(1, 2, figsize=(4, 2), layout="constrained")
axs[0].plot(np.arange(10))
axs[1].plot(np.arange(10), label='This is a plot')
axs[1].legend(loc='center left', bbox_to_anchor=(0.8, 0.5))