import numpy as np 
from matplotlib import pyplot as plt 


def egap_t_plot(
        params,
        egap_data,
        t_data, 
        errors
):
    """
    """
    x = np.linspace(
        77,297,20
    )
  
    
    y = params[0] - ((params[1]*x**2)/(params[2]+x))
    
    t_data_int = [float(a)for a in t_data]
    egap_data = [float(b) for b in egap_data]
    
    plt.errorbar(t_data_int, egap_data, label = "XK1787 ", yerr= errors, fmt='.')
    

    #lbl = r('$E_g(0)$ = ' + str(params[0]) + 'eV, $\alpha$ = ' + str(params[1]) + ', $\beta$ = ' +  str(params[2]))
    plt.plot(x, y, color = 'Red', label = 'E_g(0) = ' + str(params[0]) + 'eV, alpha = ' + str(params[1]) + ', beta = ' +  str(params[2]))
    plt.legend()
 
