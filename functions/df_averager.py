import numpy as np
import pandas as pd


def column_averager(
    DataFrame
):
    """
    Args:
        DataFrame:  pd.DataFrame(); raw data with different runs at the same temperature 

    Returns:
        av_df:      pd.DataFrame(); averaged data with one column per t 
    
    
    
    """
    list_1 = []
    list_2 = []
    av_df = pd.DataFrame()
    for column in DataFrame.columns:
        if column[-2:] == '_1':
            list_1.append(column)
        else:
            list_2.append(column)
    #print(list_1, list_2)
    for name_1, name_2 in zip(list_1,list_2):
        #print(name_1, name_2)
        short_name = name_1[:-2]
        short_name = short_name[-3:]
        name_1_list = DataFrame[name_1].to_list()
        name_2_list = DataFrame[name_2].to_list()
        av_list = (np.array(name_1_list) + np.array(name_2_list))/2
        av_df[short_name] = av_list
    # NOTE need to set av_df to a certain index, 
    # reindex_like just keeps it in the instance and doesnt change the original dataframe 
    av_df = av_df.set_index(DataFrame.index)
    return av_df

