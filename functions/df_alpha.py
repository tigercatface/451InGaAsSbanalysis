import numpy as np 
import pandas as pd 


def alphacalc(
        df_norm,
        sam_thick
):  
    
    """
    This function takes in a dataframe of normlized transmission agianst
    wavelength, then calculates the absoption coefficient from this.
    Args: 
        df_norm;    pd.DataFrame(); dataframe of normalized transmission
        sam_thick;  int; sample thickness
    """
    # Absorption coeff = log(transmission)/sample_thickness 
    alpha_df = -np.log(df_norm) / (sam_thick * 1e-7)

    return alpha_df

