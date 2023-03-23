from scipy.optimize import curve_fit
import numpy as np 


def bowing_fit(
        egap_dict,
        indiumalloy_dict
        ):
    """
    
    """
    def Bowingeq(x,b):
        #0.75*b*x**2 - x*(0.444-0.75*b)+ 0.727
        # return b*x**2 - x*(0.444-0.75*b)+ 0.727
        return 0.727*(1-x)+0.283*x- x*b*(1-x)
    
    x_list = []
    e_list = []
    for sample in egap_dict:
        # Clear global variables
        band_gap = 0
        indium_frac = 0
        # Initialize global variables 
        band_gap = egap_dict[sample]
        indium_frac = indiumalloy_dict[sample]
        e_list.append(band_gap)
        x_list.append(indium_frac)

    print(x_list)
    print(e_list)
    parameters, covarience = curve_fit(Bowingeq, x_list, e_list)
    return parameters, covarience


