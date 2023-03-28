from functions.folder_importer2 import folder_importer_os
from functions.ev_converter import ev_converter_calc
from functions.df_alpha import alphacalc
from functions.linearfit3 import linearfit3
from functions.res_plot_creator import res_data_creator
from functions.derivativecalc import deriv_calc
from matplotlib import pyplot as plt 
from functions.bowingfit2 import bowing_fit
from functions.bowing_odr import bowing_odr
import pandas as pd 
import numpy as np 

"""
        File takes in the raw data from the FTIR and calculates the
        band gap of the data with some errors. 
        This is then compared with the Energy gap function for 
        GaInAsSb/GaSb found in Vurgaftman
"""
folder_path_1 = 'data/091122_bg'
folder_path_2 = 'data/091122_2_bg'

df1 = folder_importer_os(folder_path_1)
df2 = folder_importer_os(folder_path_2)
# Ranges for Fitting FunctionsL 
sample_limits_1 = {
    'XAB1308':[0.501,0.5237],
    'XAB1309':[0.57,0.589],
    'XAB1315':[0.48, 0.506],
    'XK1786':[0.585, 0.611],
    'XK1787':[0.65, 0.678],
}
x_dict = {
     'XAB1308':0.2,
    'XAB1309':0.14,
    'XAB1315':0.25,
    'XK1786':0.1,
    'XK1787':0.05,
}

deriv_dict = {
    'XAB1308': 0.496,
    'XAB1309': 0.557,
    'XAB1315': 0.460,
    'XK1786' : 0.580,
    'XK1787' : 0.634
}

sample_name_list = ['XAB1308', 'XAB1309', 'XAB1315', 'XK1786', 'XK1787']
# Settings
A = 5  # Want figures to be A6
plt.rc('figure', figsize=[46.82 * .5**(.5 * A), 33.11 * .5**(.5 * A)])

#plt.rc('text', usetex=True)
plt.rc('font', family='serif')

# Manual Correction for the rough sides 
df1['XAB1308'] = df1['XAB1308'].apply(lambda x: x*10)

df1['XK1787'] = df1['XK1787'].apply(lambda x: x*10)

df1['XK1786'] = df1['XK1786'].apply(lambda x: x*10)

df2['XAB1308'] = df2['XAB1308'].apply(lambda x: x*10)

df2['XK1787'] = df2['XK1787'].apply(lambda x: x*10)

df2['XK1786'] = df2['XK1786'].apply(lambda x: x*10)

# Create another df and insert gaas into it: 
df1gaas = pd.DataFrame()
df2gaas = pd.DataFrame()
#print(df1.columns.tolist())
df1gaas['GaAs'] = df1['GaAs']
df2gaas['GaAs'] = df2['GaAs']
df1 = df1.drop(columns = ['GaAs'])
df2 = df2.drop(columns = ['GaAs'])

# Normalization of the data 

df1norm = df1.divide(df1gaas['GaAs'], axis = 0)
df2norm = df2.divide(df2gaas['GaAs'], axis = 0)

# Conversion to eV

df1norm = ev_converter_calc(df1norm, 1e-6)
df2norm = ev_converter_calc(df2norm, 1e-6)

# Calculation of alpha 

df_1_a = alphacalc(df1norm,1000)
df_2_a = alphacalc(df2norm,1000)

# Drop the Irrelevent data 

df_1_a = df_1_a[df_1_a.index < 0.75]
df_2_a = df_2_a[df_2_a.index < 0.75]
df_1_a = df_1_a[df_1_a.index > 0.45]
df_2_a = df_2_a[df_2_a.index > 0.45]
# Negative values are noise 
df_1_a = df_1_a.clip(lower = 0)
df_2_a = df_2_a.clip(lower = 0)

# Square them

df_1_a = np.square(df_1_a)
df_2_a = np.square(df_2_a)
# Linear fit to find band gap 
res_dict, egap_dict, errors_dict = linearfit3(df_2_a, sample_limits_1)
#print(errors_dict)
# Data creation for linear fits 
data_dict = res_data_creator(res_dict, sample_limits_1)
print(errors_dict)
# Derivative method 
df3 = df_1_a.copy()
df3.to_pickle('091122_data')
df3 = df3.rolling(500).mean()
df_deriv = deriv_calc(df3, [0.48,0.77])
df_deriv_max = df_deriv.idxmax()
# Bowing stuff now 
vurga_bowing_x = np.linspace(0,1,50)
vurga_bowing_y = 0.727*(1-vurga_bowing_x) + 0.283*vurga_bowing_x - 0.75*vurga_bowing_x*(1-vurga_bowing_x)
vurga_label = 'b = 0.75eV (Vurgaftman et al)'

# Bowing fit 
bowing_p, bowing_perror = bowing_fit(egap_dict, x_dict)
data_bowing_y = 0.727*(1-vurga_bowing_x) + 0.283*vurga_bowing_x - bowing_p[0]*vurga_bowing_x*(1-vurga_bowing_x)
bowing_deriv, bowing_deriv_error = bowing_fit(deriv_dict, x_dict)
deriv_bowing_y = 0.727*(1-vurga_bowing_x) + 0.283*vurga_bowing_x - bowing_deriv[0]*vurga_bowing_x*(1-vurga_bowing_x)
# ODR fit
#bowing_odr(egap_dict, x_dict, errors_dict)
print(r"Non-Linear least square fit b =",(bowing_p[0])," eV, $\pm$", bowing_perror[0])
e_list = []
x_list = []
e_deriv_list = []
yerrorlist = []

print('derivative', bowing_deriv[0], bowing_deriv_error[0] )
for sample in egap_dict:
    e_list.append(egap_dict[sample])
    x_list.append(x_dict[sample])
    e_deriv_list.append(deriv_dict[sample])
    yerrorlist.append(errors_dict[sample])

plt.plot(vurga_bowing_x, vurga_bowing_y,  label = r'b = 0.75eV Vurgaftman Data' )
plt.plot(vurga_bowing_x, data_bowing_y, label = 'Linear fit bowing fit')
plt.scatter(x_list, e_deriv_list,label = r'Derivative E$_g$', s = 20)
plt.plot(vurga_bowing_x, deriv_bowing_y, label = 'Derivative bowing Fit')
plt.title(r'InGaAsSb Bowing for Linear and Derivative E$_g$ Calculation Methods')
plt.ylabel(r'E$_g$ (eV)')
plt.xlabel(r'In$_x$GaAsSb Alloy fraction x')
plt.errorbar(x_list, e_list, label =r'Linear E$_g$', yerr =  yerrorlist, fmt='.', capsize= 2)

plt.legend()

plt.show()


# Plotting 
# df_1_a.replace(0,np.nan, inplace = True)
# df_1_a.plot(kind = 'line')
# plt.legend()
# for sample in data_dict:
#     plt.plot(data_dict[sample][0], data_dict[sample][1], linestyle = 'dashed', color = 'black', linewidth = 2)
# plt.suptitle(r'$\alpha^2$ for For Different GaInAsSb Samples', y=0.98, fontsize=17)
# plt.title(r'Linear fit applied to Obtain E_g', fontsize=10)
# plt.xlabel('Photon Energy (eV)')
# plt.ylabel(r'$\alpha^2 $(cm$^{-2}$)')
# plt.figure(1)
# df_deriv.plot(kind='line')
# plt.legend()
# plt.suptitle(r'd/dx[$\alpha^2$] for Different Samples', y=0.98, fontsize=17)
# plt.title(r'Smoothed using a rolling mean with a window size of 500', fontsize=10)
# plt.xlabel('Photon Energy (eV)')
# plt.ylabel(r'Differential of $\alpha^2$ (arbitraty units)')
# # plt.figure(0)
# df_1_a.plot(kind = 'line')
# plt.legend()
# plt.title('Absorption Coefficient against Photon Energy for different GaInAsSb compositions')
# plt.xlabel('Photon Energy (eV)')
# plt.ylabel(r'$\alpha^2$ $(cm^{-1})$')
# plt.yscale('log')

# plt.figure(1)
# df_2_a.plot(kind = 'line')
# plt.legend()
# plt.title('091122_2 Absorption Coeff against photon energy')
# plt.xlabel('Photon Energy (eV)')
# plt.ylabel(r'$\alpha^2$ $(cm^{-1})$')
#plt.yscale('log')


#plt.show()
