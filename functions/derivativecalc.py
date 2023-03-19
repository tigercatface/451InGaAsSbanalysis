import pandas as pd 
import numpy as np 

def deriv_calc(
        df, 
        custom_range
):
    """
    Takes a dataframe and returns the derivative of that dataframe 

    Args:
        df,         DataFrame(): alpha^2 against eV
        costum_range,List: range over which we do the thing 


    Returns:
        ddf,        DataFrame():
    """
    ddf = pd.DataFrame()    
    smol_df = df[df.index > custom_range[0]]
    smol_df = df[df.index < custom_range[1]]

    for column in smol_df:
        ev = smol_df.index.tolist()
        x = smol_df[column].tolist()
        y = []
        y = np.gradient(x, ev)
        ddf[column] = y
    ddf['eV'] = ev
    ddf = ddf.set_index('eV')


    return(ddf)


        