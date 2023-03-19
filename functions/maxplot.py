import pandas as pd 
import numpy as np 

def maximumvaluefinder(
    df,
    limits
):

    df = df[df.index > limits[0]]
    df = df[df.index < limits[1]]

    max_series = df.idxmax()
    return max_series
