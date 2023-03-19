from functions.folder_importer2 import folder_importer_os
from functions.raw_plotter import raw_plot
from functions.df_averager import column_averager
from functions.df_normalizer import df_normalizing_function
from matplotlib import pyplot as plt 
import pandas as pd
path = 'data/020223_gaas_t'
xab1315path = 'data/070223_xab1315_t'
xk1787path = 'data/090223_XK1787_t'
gaas_df = folder_importer_os(path)
xab1315_df = folder_importer_os(xab1315path)
xk1787_df = folder_importer_os(xk1787path)


xk1787_df = xk1787_df * 10
gaas_df = gaas_df[gaas_df.index < 4]
xab1315_df = xab1315_df[xab1315_df.index < 4]
xk1787_df = xk1787_df[xk1787_df.index < 4]
gaas_df = gaas_df[gaas_df.index > 1.2]
xab1315_df = xab1315_df[xab1315_df.index > 1.2]
xk1787_df = xk1787_df[xk1787_df.index > 1.2]
xab1315_df_av = column_averager(xab1315_df)
xk1787_df_av = column_averager(xk1787_df)
print('for GaAs time daddy')
# ISSUE HAPPENS HERE


gaas_df_av = column_averager(gaas_df)

xab1315_df_norm = df_normalizing_function(xab1315_df_av, gaas_df_av)
# NOTE something weird is happening with gaas_df

colour_1 = "#0dd9cb"
colour_2 = "#6e0202"
raw_plot(
    gaas_df_av,
    'GaAs Sub Raw Data',
    'Wavelength $\mu m$', 
    'SSC',
    colour_1, 
    colour_2
) 
plt.figure(1)
raw_plot(
    xab1315_df_norm,
    'XAB1315 T, Normalized',
    'Wavelength $\mu m$', 
    'SSC',
    colour_1, 
    colour_2
)
plt.figure(2)
raw_plot(
    xk1787_df_av,
    'XK1787 T',
    'Wavelength $\mu m$', 
    'SSC',
    colour_1, 
    colour_2
)

plt.show()





