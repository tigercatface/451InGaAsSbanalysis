import os
import pandas as pd
import numpy as np 

from functions.base_importer import basic_importer
"""
This file can import an entire folder worth of data in once simple go without any issues. 

Only will work for the bandgap measurements 


"""

def folder_importer_temp(
    folder_path,

):
    """
    Args: 
        folder_path;    Str; relative path of the folder
    
    """
    df = pd.DataFrame()
    # Create and clear global variables: 
    file_list =  os.listdir(folder_path)
    av_df = pd.DataFrame()

    # Create a filter to get rid of the information file labelled by:
    #file_list.pop(0)
    
    # Filter out all non text files, 
    # NOTE python 3.x returns an iterable object yet not a full list 
    # since this is a lzay method to filter items, can loop over list with values 
    # with no issues however need to be careful
    txt_files = filter(lambda x: x[-4:] == '.txt', file_list)

    # Begin to loop over txt_files 
    for sub_path in txt_files: 
        # Clear global vars: 
        full_path = ""
        sample_name = ""
        col_0 = []
        col_1 = []
        check_name = []
        # output the sample_name 
        sample_name = sub_path[7:-4]

        # get the full path 
        full_path = folder_path + '/' + sub_path

        # Use the previously created basic imported to import the file 
        # This just checks for erros
        try:
            col_0, col_1 = basic_importer(full_path)
        except:
            print('failed to load ', sample_name)
        try: 
            df[sample_name] = col_1
        except:
            print('Length Mismatch error, col_1 l = ',
                len(col_1),
                ' ',
                sample_name,
                ' ',
                'df length = ',
                len(df.index.tolist()))


    # Need to append the wavelength 
    df['col_0'] = col_0
    df = df.set_index('col_0')
    # print('column appended')
    # # Need to loop over the columns of the dataframes to find an average between the two columns 
    # # Create two lists, one with 1 in the end and one with 0 
    # list_1 = []
    # list_2 = []

    # for column in df.columns:
    #     if column[-2:] == '_1':
    #         list_1.append(column)
    #     else:
    #         list_2.append(column)
    # print(list_1)
    # for name_1, name_2 in zip(list_1,list_2):
    #     short_name = name_1[:-2]
    #     # NOTE: write 097 070 etc
    #     # NOTE: where the fuck is 77 90 etc
    #     short_name = short_name[-3:]
    #     name_1_list = df[name_1].to_list()
    #     name_2_list = df[name_2].to_list()
    #     av_list = (np.array(name_1_list) + np.array(name_2_list))/2
    #     av_df[short_name] = av_list

    # av_df['col_0'] = col_0
    # av_df = av_df.set_index('col_0')
    
    
    return df
