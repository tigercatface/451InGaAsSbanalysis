from scipy.optimize import curve_fit
import numpy as np 


def bowing_fit(
        egap_dict,
        indiumalloy_dict
        ):
    """
    
    """
    # Nested functions 
    def test(x,b):
        #return -b*x*(1-x) + 0.727(1-x) + 0.283(x)
        return np.poly1d(b, -0.444-b, 0.727)
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
    param, param_cov = curve_fit(test, x_list, e_list)

