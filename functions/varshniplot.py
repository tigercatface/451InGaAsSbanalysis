import numpy as np 
from matplotlib import pyplot as plt 


def egap_t_plot(
        params,
        egap_data,
        t_data
):
    """
    """
    x = np.linspace(
        77,297,20
    )
  
    
    y = params[0] - ((params[1]*x**2)/(params[2]+x))
    
    t_data_int = [int(a)for a in t_data]
    ax = plt.axes()
    ax.scatter(t_data_int, egap_data, label = "Data")
    ax.plot(x, y)
 