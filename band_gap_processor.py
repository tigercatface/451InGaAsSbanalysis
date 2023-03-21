from functions.folder_importer2 import folder_importer_os
from functions.raw_plotter import raw_plot
from functions.df_normalizer import df_normalizing_function
from functions.ev_converter import ev_converter_calc
from functions.df_alpha import alphacalc
from functions.raw_plotter import raw_plot
from functions.alpha_plot import a_plot
from matplotlib import pyplot as plt 

import pandas as pd 
import numpy as np 



colour_1 = "#0dd9cb"
colour_2 = "#6e0202"
"""This file imports all the data and then processes it all together to calculate the band gap"""

folder_path_5 = 'data/091122_bg'

df1 = folder_importer_os(folder_path_5)

#df['quantity'] = df['quantity'].apply(lambda x: x*-1)
#C:\Users\roman\Desktop\mastersproject-20230301T143517Z-001\mastersproject\data
# Manual correction for the rough sides 

df1['XAB1308'] = df1['XAB1308'].apply(lambda x: x*10)

df1['XK1787'] = df1['XK1787'].apply(lambda x: x*10)

df1['XK1786'] = df1['XK1786'].apply(lambda x: x*10)

print(df1)

# Change the index ranges 

df1 = df1[df1.index < 5]
df1 = df1[df1.index > 1.5]

# Create another df and manipulate the gaas data into it 

df2 = pd.DataFrame()
df2['GaAs'] = df1['GaAs']
df1 = df1.drop(columns = ['GaAs'])

# Normalization of the data 
df3 = df1.divide(df2['GaAs'], axis = 0)  

df_a = ev_converter_calc(df3, 1e-6)
df_a = alphacalc(df_a, 1000)

raw_plot(df_a, '091122 Absroption Coefficient plot', 'eV', '\alpha (cm^{-1})', colour_1, colour_2)
plt.figure(1)
df_a = np.square(df_a)
a_plot(df_a,'091122 Absroption Coefficient plot', 'eV', r'\alpha (cm^{-1})', colour_1, colour_2)
plt.show()


