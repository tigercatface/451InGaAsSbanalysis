import pandas as pd 
import numpy as np 


def rolling_averager(
    df, 
    window_size
):
    """
    """

    df_rolled = pd.DataFrame()

    for column in df.columns:
        df_rolled[column] = df.rolling(window_size).mean()
    df_rolled = df_rolled.set_index(df.index.tolist()) 
    df.dropna(inplace = True)

    return df_rolled