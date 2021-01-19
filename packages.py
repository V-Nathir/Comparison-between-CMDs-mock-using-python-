import numpy as np
import pandas as pd;pd.options.mode.chained_assignment = None 
import csv,time,random;
from scipy import stats
from scipy.stats import norm
import openturns as ot 
from progress.bar import ChargingBar
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.colors as mcol
import matplotlib.patches as mpatches
import matplotlib.cm as cm
import matplotlib

plt.rcParams.update({
    "lines.color": "white",
    "patch.edgecolor": "black",
    "text.color": "white",
    "axes.facecolor": "black",
    "axes.edgecolor": "lightgray",
    "axes.labelcolor": "white",
    "xtick.color": "white",
    "ytick.color": "white",
    "grid.color": "lightgray",
    "figure.facecolor": "black",
    "figure.edgecolor": "black",
    "savefig.facecolor": "black",
    "savefig.edgecolor": "black"})
