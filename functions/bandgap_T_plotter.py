import pandas as pd 
import numpy as np 
from matplotlib import pyplot as plt 

def egap_plot(
    df,
    title,
    xlabel,
    ylabel,
):
    plt.scatter(list(df.index), df.values)
    plt.title(title)

    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
