import pandas as pd 
import numpy as np 
from scipy import stats
from matplotlib import pyplot as plt 

def linearfit3(
        df,
        sample_limits
):
    """
    args:
        dataframe,          DataFram: df of alpha^2 , eV index, 
        sample_limits,      Dict: Key: Sample name, value: [lowerlim,upperlim]
    returns:
        res_dict,           Dict, results of fit 
        egap_dict,          Dict, egap
        errors_dict,        Dict,
    """

    egap_dict = {}
    res_dict = {}
    errors_dict = {}
    for sample in sample_limits:
        df1 = pd.DataFrame()
        df2 = df.copy()
        y = 0
        x = 0
        egap = 0
        lowlim = 0
        upplim = 0
        errors = 0
        lowlim = sample_limits[sample][0] # 1st element of list, 
        upplim = sample_limits[sample][1] # 2nd element of list, 
        # import the df 
        df1 = df2[[sample]].copy()
        # New special limits
        df1 = df1[df1.index > lowlim]
        df1 = df1[df1.index < upplim]
        y = df1[sample].tolist()
        x = df1.index.tolist()
        res = stats.linregress(x,y)
        # y = mx+c => x = -c/m
        egap = -(res.intercept/res.slope)
        errors = np.sqrt(np.square(res.stderr/res.slope ))
        #errors = np.sqrt(errors)
        errors_dict[sample] = errors
        egap_dict[sample] = egap
        res_dict[sample] = res
    print(egap_dict)
    return res_dict, egap_dict, errors_dict
