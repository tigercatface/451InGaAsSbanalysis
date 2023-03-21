import pandas as pd 
import numpy as np 
from matplotlib import pyplot as plt 
from functions.alpha_plot import a_plot
from functions.singlecol_df import single_col_fun
from functions.linearfitold import linearfit2
from functions.varshniparamcalcl import varshni_fit
from functions.bandgap_T_plotter import egap_plot
colour_1 = "#0dd9cb"
colour_2 = "#6e0202"

xk7ranges = {
    '077':[0.7078,0.7255],
    '090':[0.7062,0.723],
    '110':[0.7070,0.7188],
    '130':[0.6919,0.7036],
    '150':[0.6877,0.7053],
    '170':[0.68430,0.6961],
    '190':[0.6792,0.6919],
    '210':[0.6708,0.6860],
    '230':[0.6635,0.6804],
    '250':[0.6585,0.6719],
    '270':[0.6493,0.6641],
    '297':[0.6414,0.6574]
}
t_names = [
    '077',
    '090',
    '110',
    '130',
    '150',
    '170',
    '190',
    '210',
    '230',
    '250',
    '270',
    '297'
]
xk7 = pd.read_pickle('xk1787_aev')

xk7 = xk7[xk7.index > 0.55]

xk7 = np.square(xk7)
t = '297'
min_xk7 = xk7.min()
xk7_s = xk7.subtract(min_xk7)
#xk_single = single_col_fun(xk7_s, t)
#plt.plot(xk_single.index, xk_single[t])
sample_regression_dict, sample_df_dict, egap_dict = linearfit2(xk7_s, t_names, xk7ranges)

xk7_t = list(egap_dict.keys())
xk7_e = list(egap_dict.values())
xk_et_df = pd.Series(xk7_e, index= xk7_t)
xk1787_params, xk1787_cov = varshni_fit(xk7_t, xk7_e)
plt.figure(1)
egap_plot(xk_et_df, '1', 'temp', 'bandgaps')
plt.show()