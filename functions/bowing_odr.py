import numpy as np 
from scipy.odr import ODR, Model, Data, RealData

def bowing_odr(
    egap_dict,
    indium_alloy_dict,
    errors_dict
):
    def Bowingeq(x,b):
        #0.75*b*x**2 - x*(0.444-0.75*b)+ 0.727
        # return b*x**2 - x*(0.444-0.75*b)+ 0.727
        return 0.727*(1-x)+0.283*x- x*b*(1-x)
    x_list = []
    e_list = []
    error_list = []
    for sample in egap_dict:
        # Clear global variables
        band_gap = 0
        indium_frac = 0
        std_error = 0
        # Initialize global variables 
        band_gap = egap_dict[sample]
        indium_frac = indium_alloy_dict[sample]
        std_error = errors_dict[sample]
        # Append global globvars
        e_list.append(band_gap)
        x_list.append(indium_frac)
        error_list.append(std_error)
    bowing =  Model(Bowingeq)
    sx = [0.01,0.01,0.01,0.01,0.01]
    bowing_data = RealData(x_list,e_list, sx = sx ,sy = error_list)
    bowing_odr = ODR(bowing_data,bowing,beta0=[1])
    bowing_output = bowing_odr.run()
    bowing_output.pprint()

