import pandas as pd 
from functions.folder_importer2 import folder_importer_os
from functions.df_averager import column_averager
from functions.df_normalizer import df_normalizing_function
from functions.df_alpha import alphacalc
from functions.ev_converter import ev_converter_calc
from matplotlib import pyplot as plt 
import numpy as np 
import os 
xab1309 = 'data/160323_XAB1309_t'
gaas_080323_gaas_t = 'data/080323_gaas_t'
gaas_080323_gaas_t = 'data/020223_gaas_t'


gaas = folder_importer_os(gaas_080323_gaas_t)

xab1309 = pd.read_pickle('xab1309_raw')
#print(xab1309)
gaas = gaas[gaas.index < 5]
gaas = gaas[gaas.index > 1]
xab1309 = xab1309[xab1309.index < 5]
xab1309 = xab1309[xab1309.index > 1]

# Average the columns 
xab1309 = column_averager(xab1309)
gaas = column_averager(gaas)

#print(xab1309)
# Normalize the columns
xab1309_n = df_normalizing_function(xab1309, gaas)

# # Alpha calc
xab1309_a = alphacalc(xab1309_n, 1000)

# # ev converter 
xab1309_ev_a = ev_converter_calc(xab1309_a, 1e-6)
xab1309_ev_a.to_pickle('xab1309_df_a_ev')

# plotter checkers 
xab13092 = np.square(xab1309_ev_a)
xab13092.plot(kind = 'line')
plt.yscale('log')

# print(xab1309_ev_a)
# plt.figure(2)

# gaas.plot(kind = 'line')

plt.show()
x