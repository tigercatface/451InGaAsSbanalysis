
from pylab import *
from matplotlib import pyplot as plt 
import numpy as np 
import pandas as pd 

# TODO:
#   1. Add an option to chose weather to multiply by 10 or not, 
#   2. Add a nmumber choice between energy and lambda 

def alphaplot(
    control_path, 
    sample_path_list, 
    sample_name_list,
    thickness_list, 
    control_thickness,
    control_name,
    title,
    upperlimit,
    lowerlimit,
    multiply,
    units,
    ):

    # Import control values as lists to normalize data with 
    con_nm, con_t = loadtxt(control_path, unpack = True)
    # Create the absorption coefficient of the control substance 
    con_t = [abs(number) for number in con_t]
    alpha_c = -np.log(con_t) / (
        control_thickness * 1e-7
    )
    # Create the dataframe to store the stuff in 
    df = pd.DataFrame()
    df[control_name] = alpha_c
    # Create the wavelength and turn it to the appendix 
    df['lambda'] = con_nm
    df = df.set_index('lambda')
    
    # Need to have an energy conversion one, 
    h = 4.1357e-15 #eV s
    c = 299792458 # ms-1
    #NOTE 
    # Assuming wavelength is in um,
    con_ev = [h*c/(m*1e-6) for m in con_nm]
    df['energy'] = con_ev
    # Loop over list of sample path 
    for i in range(len(sample_path_list)):
        # Preallocate memory and clear datam from lists 
        sam_nm  = []
        sam_t = []
        # Memory for values 
        sample_path = sample_path_list[i]
        thickness = thickness_list[i]
        sample_name = sample_name_list[i]
        # Import data 
        sam_nm, sam_t = loadtxt(sample_path, unpack = True)
        # Jerry fix to make all the data equal
           # Check if multiply by 10 is set to true
        if i < 3:
            if multiply == True:
                sam_t = [m * 10 for m in sam_t]
        # Normalize the data 
        norm_t =  [m/n for m,n in zip(sam_t, con_t)]
        # Absorption coefficient
        alpha = -np.log(norm_t) / (
            thickness * 1e-7)
        # Plot the values 
        if units != 0:
            plt.figure(0)
            plt.plot(con_ev, norm_t, label = sample_name)
            plt.figure(1)
            plt.plot(con_ev, alpha, label = sample_name)
        else:
            plt.figure(0)
            plt.plot(sam_nm, norm_t, label = sample_name)
            plt.figure(1)
            plt.plot(sam_nm, alpha, label = sample_name)

        # Append the values to a pandas dataframe 
        df[sample_name] = alpha
    
    plt.figure(0)
    if units !=0:
        plt.plot(con_ev, con_t, label = control_name)
        plt.xlabel('Photon Energy (eV)')
    else:
        plt.plot(con_nm, con_t, label = control_name)
        plt.xlabel('Wavelength (micrometers)')
    plt.yscale('log')
    plt.legend()
    plt.title('Normalyzed Transmission Data')
    plt.ylabel('Tramsmission (Ratio)')
    if units != 0:
        loweelimit = h*c/(lowerlimit * 1e-6)
        highelimit = h*c/(upperlimit * 1e-6)
        plt.xlim(loweelimit,highelimit),
    else:
        plt.xlim(lowerlimit, upperlimit)
    


    plt.figure(1)
    if units != 0:
        plt.plot(con_ev, alpha_c, label = control_name)
        plt.xlabel('Photon Energy (eV)')
    else:
        plt.plot(con_nm, alpha_c, label = control_name)
        plt.xlabel('Wavelength (micrometers)')
    plt.yscale('log')
    plt.legend()
    plt.title(title)
    if units != 0:
        loweelimit = h*c/(lowerlimit * 1e-6)
        highelimit = h*c/(upperlimit * 1e-6)
        plt.xlim(loweelimit,highelimit),
    else:
        plt.xlim(lowerlimit, upperlimit)
    
    return df

