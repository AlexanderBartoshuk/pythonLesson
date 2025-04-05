import matplotlib.pyplot as plt
import numpy as np


# Helper function used for visualization in the following examples
def identify_axes(ax_dict, fontsize=48):
    """
    Helper to identify the Axes in the examples below.

    Draws the label in a large font in the center of the Axes.

    Parameters
    ----------
    ax_dict : dict[str, Axes]
        Mapping between the title / label and the Axes.
    fontsize : int, optional
        How big the label should be.
    """
    kw = dict(ha="center", va="center", fontsize=fontsize, color="darkgrey")
    for k, ax in ax_dict.items():
        ax.text(0.5, 0.5, k, transform=ax.transAxes, **kw)

    
np.random.seed(19680801)
hist_data = np.random.randint(1_500)

fig = plt.figure(layout='constrained')
ax_array = fig.subplots(2,2,squeeze=False)

ax_array[0,0].bar(['a','b','c'],[5,7,9])
ax_array[0,1].plot([1,2,3])
ax_array[1,0].hist(hist_data, bins='auto')
ax_array[1, 1].imshow([[1, 2], [2, 1]])

identify_axes(
    {(j,k): a for j,r in enumerate(ax_array) for k, a in enumerate(r)}
)


fig = plt.figure(layout='constrained')
ax_dict = fig.subplot_mosaic(
    [
        ['bar','plot'],
        ['hist', 'image']
    ]
)
ax_dict['bar'].bar(["a", "b", "c"], [5, 7, 9])
ax_dict['plot'].plot([1,2,3])
ax_dict['hist'].hist(hist_data)
ax_dict['image'].imshow([[1,2],[2,1]])
identify_axes(ax_dict)


mosaic = 'AB;CD'


fig = plt.figure(layout='constrained')
ax_dict = fig.subplot_mosaic(mosaic)
identify_axes(ax_dict)


axd = plt.figure(layout='constrained').subplot_mosaic(
    """
    ABD
    CCD
    """
)
identify_axes(axd)


axd = plt.figure(layout='constrained').subplot_mosaic(
    """
    A.C
    BBB
    .D.
    """
)
identify_axes(axd)


axd = plt.figure(layout='constrained').subplot_mosaic(
    """
    .a.
    bAc
    .d.
    """,
    height_ratios=[1,3.5,1], 
    width_ratios=[1,3.5,1],
)
identify_axes(axd)

axd = plt.figure(layout='constrained').subplot_mosaic(
    'AB', subplot_kw={'projection':'polar'}
)
identify_axes(axd)



