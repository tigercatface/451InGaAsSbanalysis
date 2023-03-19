from functions.folder_importer2 import folder_importer_os
from functions.df_normalizer import df_normalizing_function
from functions.ev_converter import ev_converter_calc
from functions.df_alpha import alphacalc
from functions.linearplot import linearfit
from functions.linearfitold import linearfit2
from matplotlib import pyplot as plt 

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
sample_limits = {
    'XAB1308':[0.501,0.5237],
    'XAB1309':[0.57,0.589],
    'XAB1315':[0.48, 0.506],
    'XK1786':[0.585, 0.611],
    'XK1787':[0.65, 0.678],
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
print(df1.columns.tolist())
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

df_1_a = df_1_a[df_1_a.index < 0.8]
df_2_a = df_2_a[df_2_a.index < 0.8]
df_1_a = df_1_a[df_1_a.index > 0.4]
df_2_a = df_2_a[df_2_a.index > 0.4]
# Negative values are noise 
df_1_a = df_1_a.clip(lower = 0)
df_2_a = df_2_a.clip(lower = 0)

# Square them

df_1_a = np.square(df_1_a)
df_2_a = np.square(df_2_a)

# Linear fit to find band gap 

sample_regression_dict, egap_dict = linearfit(df_1_a, sample_limits)
print(egap_dict)
sample_regression_dict_2, sample_df_dict_2, egap_dict_2 = linearfit2(df_1_a, sample_name_list, sample_limits)

print(egap_dict_2)
# plt.figure(0)
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
plt.show()