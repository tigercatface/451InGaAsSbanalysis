import os
import pandas as pd
from functions.base_importer import basic_importer
"""
This file can import an entire folder worth of data in once simple go without any issues. 

Only will work for the bandgap measurements 


"""

def folder_importer_os(
    folder_path,

):
    """
    Args: 
        folder_path;    Str; relative path of the folder
    
    """
    df = pd.DataFrame()
    # Create and clear global variables: 
    file_list =  os.listdir(folder_path)
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
        
        # Quick check for the 10 issue 
        # harder now since we may have sample_1 or sample_2 
        # use the fact that the maximum length of the name canm only be 7 hence 
        # NOTE this jerry fix will break if _01 or _001
        # only works for _1

        # 
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

    return df




