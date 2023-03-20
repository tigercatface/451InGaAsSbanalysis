import pandas as pd 
import numpy as np 
from scipy.optimize import curve_fit

def varshni_fit(
        xdata,
        ydata
):
    """
    """
    # Nested function to be fit 

    def Varshinieeq(x,e0,a,b):
        y = (e0 - (a*x**2)/(x+b))
        return y
    
    parameters, covarience = curve_fit(Varshinieeq, xdata, ydata)
    return parameters, covarience