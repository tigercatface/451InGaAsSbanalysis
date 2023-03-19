import numpy as np 
import pandas as pd 

def df_separator(
    DataFrame
):
    separated_df_1 = pd.DataFrame()
    separated_df_2 = pd.DataFrame()

    for column in DataFrame.columns:
        column_name = ''
        items = []

        items = DataFrame[column].to_list()
        column_name = column[:2]
        column_name = column_name[-3:]

        if column[-2:] == '_1':
            separated_df_1[column] = items
        if column[-2:] == '_2':
            separated_df_2[column] = items

    return separated_df_1, separated_df_2

    


