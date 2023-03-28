import pandas as pd 
import numpy as np 
from matplotlib import pyplot as plt 
from functions.alpha_plot import a_plot
from functions.singlecol_df import single_col_fun
from functions.linearfitold import linearfit2
from functions.linearfit3 import linearfit3
from functions.varshniparamcalcl import varshni_fit
from functions.bandgap_T_plotter import egap_plot
from functions.varshniplot import egap_t_plot
colour_1 = "#0dd9cb"
colour_2 = "#6e0202"
A = 5
plt.rc('figure', figsize=[46.82 * .5**(.5 * A), 33.11 * .5**(.5 * A)])

#plt.rc('text', usetex=True)
plt.rc('font', family='serif')
t = '110'
xk7ranges = {
    '077':[0.713, 0.726],
    '090':[0.707,0.724],
    '110':[0.706,0.721],
    '130':[0.700,0.714],
    '150':[0.695,0.706],
    '170':[0.689,0.700],
    '190':[0.681,0.692],
    '210':[0.672,0.685],
    '230':[0.666,0.678],
    '250':[0.659,0.672],
    '270':[0.655,0.672],
    '297':[0.645,0.653]
}
# NOTE lauras values are different to mine so will have to re-evaluate them 

xk7lauraranges = {
    '077':[0.708,0.725],
    '090':[0.707,0.708],
    '110':[0.702,0.714],
    '130':[0.7,0.713],
    '150':[0.693,0.71],
    '170':[0.686, 0.697],
    '190':[0.68, 0.692],
    '210':[0.673,0.685],
    '230':[0.666,0.679],
    '250':[0.66,0.67],
    '270':[0.653,0.665],
    '297':[0.645,0.66]
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
    '270'
 #   '297'
]
xk7 = pd.read_pickle('xk1787_aev')

xk7 = xk7[xk7.index > 0.55]

xk7 = np.square(xk7)
min_xk7 = xk7.min()
xk7_s = xk7.subtract(min_xk7)
# xk_single = single_col_fun(xk7_s, t)
# #plt.figure(0)
# plt.plot(xk_single.index, xk_single[t])

print(xk7_s)
sample_regression_dict, egap_dict, errors_dict1 = linearfit3(xk7_s, xk7ranges)
print(xk7_s)
xk7laura_res, xk7laura_egap, xk7laura_errors = linearfit3(xk7_s, xk7lauraranges) 
print(xk7_s)
xk7me_res, xk7me_egap, xk7me_errors = linearfit3(xk7_s, xk7ranges)
xk7_t = list(egap_dict.keys())
xk7_e = list(egap_dict.values())

xk7_l_t = list(xk7laura_egap.keys())
xk7_l_e = list(xk7laura_egap.values())
xk7_et_l_df= pd.DataFrame()
xk7_et_l_df['Band Gap'] = xk7_l_e
xk7_et_l_df['Temp'] = xk7_l_t


xk7_m_t = list(xk7me_egap.keys())
xk7_m_e = list(xk7me_egap.values())
xk7_m_errors = list(xk7me_errors.values())
xk7_et_m_df= pd.DataFrame()
xk7_et_m_df['Band Gap'] = xk7_m_e
xk7_et_m_df['Temp'] = xk7_m_t
xk7_m_t = [int(a) for a in xk7_m_t]
xk_et_df = pd.DataFrame()
# xk_et_df['Band Gap'] = xk7_e
# xk_et_df['Temp'] = xk7_t
xk1787_params, xk1787_cov = varshni_fit(xk7_t, xk7_e)

xk1787_params_l, xk1787_cov_l = varshni_fit(xk7_l_t, xk7_l_e)
xk1787_params_m, xk1787_cov_m = varshni_fit(xk7_m_t, xk7_m_e)

#plt.figure(2)
plt.figure(0)
# #xk_et_df.plot.scatter(x = 'Band Gap', y = 'Temp', s = 20, c = 'Red', label = 'XK1787')
# plt.title(r'Band Gap aganist T for XK1787, In$_{0.05}$GaAsSb')
# plt.xlabel('Temperature (K)')
# plt.ylabel(r'Band Gap E$_g$ (eV)')
# # egap_t_plot(xk1787_params, xk7_e, xk7_t)
# # egap_t_plot(xk1787_params_l, xk7_l_e, xk7_l_t)
# plt.scatter(xk7_l_t, xk7_l_e, s = 15, label = 'Lauras analysis')
# plt.scatter(xk7_m_t, xk7_m_e, s = 15, label = 'My analysis')
# plt.legend()
# plt.title(r'Band Gap aganist T for XK1787, In$_{0.05}$GaAsSb')
# plt.xlabel('Temperature (K)')
# plt.ylabel(r'Band Gap E$_g$ (eV)')

# NOTE new df plot for other stuff 
plt.title(r'Band Gap aganist T for XK1787, In$_{0.05}$GaAsSb')
plt.xlabel('Temperature (K)')
plt.ylabel(r'Band Gap E$_g$ (eV)')
# plt.scatter(xk7_m_t, xk7_m_e, s = 15, label = 'My analysis')
egap_t_plot(xk1787_params, xk7_e, xk7_t, xk7_m_errors)
# plt.legend()
# plt.title(r'Band Gap aganist T for XK1787, In$_{0.05}$GaAsSb')
# plt.xlabel('Temperature (K)')
# plt.ylabel(r'Band Gap E$_g$ (eV)')
plt.show()