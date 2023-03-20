import numpy as np 
from matplotlib import pyplot as plt
import scipy.stats as stats

# NOTE 

# REDO ALL OF THE LINEAR FITS AND USE FUCKING SCIPY U DAFT CUNT 

"""
This file takes the values found in vurgafftman and plots them
onto a graph. 

The energy gap list combined with the alloy fraction list is used 
to compare the two bowing graphs 

TODO:
    
    Create a fitting function for vurgafftmans equation using the 5
    values of data we have 

"""

def bowing_plotter( 
    egap, 
    error,
    z, 
    sample_names

):
    """
    Args: 
        egap:   str: egap of the samples in the correct order  
        errors: dict: sample against errors 
        z:      str: alloy fractionm of the samples in the correct order
    """

    # NOTE 

    print(error)
    z_x = np.arange(0,1,1e-4)
    e_y_v = 0.727*(1-z_x) + 0.283*z_x - 0.75*z_x*(1-z_x)
    plt.figure(5)
    
    # NOTE Vurgaftman has no bitches, I meant errors..... 
    plt.plot(z_x, e_y_v, label = 'Vurgaftman Bowing5 Parameters')
    # Now we want to loop over the list of names so we get a correctly ordered list of
    # band gaps and alloy fractions for the correct samples. 
    z_list = []
    e_list = []
    e_e_max = []
    e_e_min = []
    for name in sample_names:
        e = 0
        coolz = 0 
        e = egap[name]
        coolz = z[name]
        e_list.append(e)
        z_list.append(coolz)
        e_e_max.append(error[name][0])
        e_e_min.append(error[name][1])
    e_e = [e_e_max,e_e_min]

    plt.scatter(z_list, e_list, label = 'Band_gap for Samples', marker= '+', c = 'red')
    plt.errorbar(z_list, e_list, yerr = e_e, fmt="o", capsize=3)   
    # TODO produce the linear fit of the data and see what happens, 
    model = np.polyfit(z_list, e_list, 2) #np.poly1d

    fit_x = np.arange(0,1,1e-4)
    fit_y = model[0] * fit_x ** 2 + model[1] * fit_x + model[2]

    

    
    plt.plot(fit_x, fit_y, label = 'Quadratic FIt')
    plt.title(r'Band Gap against Alloy Fraction')
    plt.legend()
    plt.ylabel(r'Band Gap Energy $E_{g}$, (eV)')
    
    plt.xlabel(r'Alloy Fraction z for $(GaSb)_{1-z}(InAs_{0.91}Sb_{0.09})_{z}$ ')

    print(model)
