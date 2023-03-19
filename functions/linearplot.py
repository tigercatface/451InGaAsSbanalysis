import pandas as pd 
import numpy as np
import statsmodels.api as sm 

def linearfit(
        df,
        limits_dict
):
    """ Function fits a linear fit between the specified points in the df 
    args:
        df,             pd.DataFrame(): df od alpha^2, eV index
        limits_dict,    Dict: Key: Temp, Value : [lowelim, Upperlim]
    returns
        sample_regression_dict: Dict, key: T,. Returns: regression fits results,
        egap_dict:              Dict, Key: T, Returns: Band Gap results
    """
    egap_dict = {}
    sample_regression_dict = {}
    
    for sample in limits_dict:
        y = 0
        x = 0
        lowlim = 0
        upplim = 0

        lowlim = limits_dict[sample][0]
        highlim = limits_dict[sample][1]
        # Create empty dataframe to apply new limits to 
        df1 = pd.DataFrame()
        # Copy of dataframe to not fuck with it  
        dfcopy = df[[sample]].copy()
        # New special limits
        df1 = dfcopy[dfcopy.index > lowlim]
        df1 = dfcopy[dfcopy.index < lowlim]
        y = df1[sample].tolist()
        x = df1.index.tolist()
        model = sm.OLS(y, sm.add_constant(x))
        results = model.fit()
        sample_regression_dict[sample] = results.summary()
        #print(results.summary)
        fit_m = results.params[1]
        fit_b = results.params[0]
        egap = - fit_b / fit_m 
        print(sample, ' Band Gap is: ', egap, 'eV')

        egap_dict[sample] = egap
    return sample_regression_dict, egap_dict


