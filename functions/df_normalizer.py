import numpy as np 
import pandas as pd 

def df_normalizing_function(
    sample_df,
    substrate_df
    ):
    """
    Args:
        sample_df:      pd.DataFrame(); df of sample data averaged already
        substrate_df:   pd.DataFrame(); df of sample data averaged already  

    """
    if len(sample_df.columns) != len(substrate_df.columns):
        print('Columns in the sample_df:')
        print(sample_df.columns)
        print('Columns in substrate_df:')
        print(substrate_df.columns)
        raise ValueError('Lengths of df_columns do not match something has gone wrong before')
    
    df_norm = pd.DataFrame()

    df_norm =  sample_df.div(substrate_df)
    return df_norm
