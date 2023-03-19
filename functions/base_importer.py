
import numpy as np
from pylab import *


"""
This file imports the raw data and will return two lists

"""

def basic_importer(
    filepath
):
    """
    File imports raw data and separates it into two lists
    Args:
        filepath:   str; relative filepath of the data 

    Returns:
        col_0:      list; values in column 0
        col_1:      list; values in column 1 
    """

    # Clear some global variables
    col_0 = []
    col_1 = []

    # Import the data 
    col_0, col_1 = loadtxt(filepath, unpack = True)

    print('Loaded data from:', filepath, ', succesfully!')
    return col_0, col_1


