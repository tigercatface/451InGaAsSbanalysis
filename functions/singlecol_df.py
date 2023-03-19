import pandas as pd 
import numpy as np 

def single_col_fun(
    df,
    value
        
):
    """
    This funciton converts the whole df to one value for 
    easier determination of limits for the linearfit 
    function that will be applied later 
    Args: 
        df:     pd.DataFrame(); df of absorption coeff against energy
        value:  str(); value of column that I want to analyze
    
    """
    df_one  = pd.DataFrame()
    df_one[value] = df[value]

    return df_one


