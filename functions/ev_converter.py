import numpy as np 
import pandas as df 

def ev_converter_calc(
        df, 
        m
):
    """
    Converts  from wavelength to photon energy 

    Args: 
        df: pd.DataFrame(); df that wants to be converted with wavelength in the index 
        m:  float; scale of the index, 1e-6 for micrometers 
    """
    h = 4.1357e-15 #eV s
    c = 299792458 # ms-1
    
    wavelength = df.index.tolist()
    ev = [h*c/ (i*m) for i in wavelength]
    df['eV'] = ev
    df = df.set_index('eV')

    return df

    
