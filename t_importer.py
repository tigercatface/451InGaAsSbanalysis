from functions.folder_importer2 import folder_importer_os
from functions.raw_plotter import raw_plot
from functions.df_averager import column_averager
from functions.df_normalizer import df_normalizing_function
from functions.df_alpha import alphacalc
from functions.ev_converter import ev_converter_calc
from functions.alpha_plot import a_plot
from functions.singlecol_df import single_col_fun
from functions.linearplot import linearfit
from functions.derivativecalc import deriv_calc
from functions.rollingaverage import rolling_averager
from functions.maxplot import maximumvaluefinder
from functions.bandgap_T_plotter import egap_plot
from functions.varshniparamcalcl import varshni_fit
from functions.varshniplot import egap_t_plot
from matplotlib import pyplot as plt 

import pandas as pd
import numpy as np 

colour_1 = "#0dd9cb"
colour_2 = "#6e0202"

path = 'data/080323_gaas_t'
xab1315path = 'data/070223_xab1315_t'
xk1787path = 'data/090223_XK1787_t'

gaas_020223_gaas_t = 'data/020223_gaas_t'
gaas_080323_gaas_t = 'data/080323_gaas_t'

xab1315_params_dict = {
    '077': [0.498, 0.535],
    '090': [0.494, 0.532],
    '110': [0.493, 9.530],
    '130': [0.491, 9.525],
    '150': [0.491, 0.520],
    '170': [0.493, 0.511],
    '190': [0.492, 0.507],
    '210': [0.491, 0.503],
    '230': [0.490, 0.503],
    '250': [0.489, 0.504],
    '270': [0.500, 0.507],
    '297': [0.492, 0.511],
}

xab1315_custom_range = [0.45, 0.55]
xk1787_custom_range = [0.7, 0.73]
xk1787_params_dict = {
    '077': [0.66, 0.689],
    '190': [0.66, 0.691],
    '210': [0.66, 0.68],
    '230': [0.65, 0.675],
    '250': [0.648, 0.669],
    '270': [0.645, 0.669],
    '297': [0.634, 0.65],
}

# Import the shit

# gaas_df = folder_importer_os(path)

# xab1315_df = folder_importer_os(xab1315path)

# xk1787_df = folder_importer_os(xk1787path)

# gaas_020223 = folder_importer_os(gaas_020223_gaas_t)

# gaas_080223 = folder_importer_os(gaas_080323_gaas_t)


# # x10 for the xk1787
# xk1787_df = xk1787_df * 10

# # Changing the index ranges 
# gaas_df = gaas_df[gaas_df.index < 5]
# xab1315_df = xab1315_df[xab1315_df.index < 5]
# xk1787_df = xk1787_df[xk1787_df.index < 5]
# gaas_020223 = gaas_020223[gaas_020223.index < 5]
# gaas_080223 = gaas_080223[gaas_080223.index < 5]


# gaas_df = gaas_df[gaas_df.index > 1]
# xab1315_df = xab1315_df[xab1315_df.index > 1]
# xk1787_df = xk1787_df[xk1787_df.index > 1]
# gaas_020223 = gaas_020223[gaas_020223.index > 1]
# gaas_080223 = gaas_080223[gaas_080223.index > 1]

# # Average the columns
# xab1315_df_av = column_averager(xab1315_df)
# xk1787_df_av = column_averager(xk1787_df)
# gaas_df_av = column_averager(gaas_df)
# gaas_020223_av = column_averager(gaas_020223)
# gaas_080323_av = column_averager(gaas_080223)


# xab1315_df_norm_1 = df_normalizing_function(xab1315_df_av, gaas_020223_av)


# xab1315_df_norm_2 = df_normalizing_function(xab1315_df_av, gaas_080323_av)
# xk1787_df_norm = df_normalizing_function(xk1787_df_av, gaas_080323_av)

# xab1315_df_a_1 = alphacalc(xab1315_df_norm_1, 1000)
# xab1315_df_a_2 = alphacalc(xab1315_df_norm_2, 1000)
# xk1787_df_a = alphacalc(xk1787_df_norm, 1000)

# xab1315_df_a_ev_1 = ev_converter_calc(xab1315_df_a_1, 1e-6)
# xab1315_df_a_ev_2 = ev_converter_calc(xab1315_df_a_2, 1e-6)
# xk1787_df_a_ev = ev_converter_calc(xk1787_df_a, 1e-6)
# # NOTE working with pickles from here 
# xk1787_df_a_ev.to_pickle("xk1787_aev")
# xab1315_df_a_ev_1.to_pickle("xab1315_1aev")
# xab1315_df_a_ev_2.to_pickle("xab1315_2av")

xk1787_df_a_ev_2 = pd.read_pickle("xk1787_aev")
xab1315_df_a_ev_1 = pd.read_pickle("xab1315_1aev")
xab1315_df_a_ev_2 = pd.read_pickle("xab1315_2av")

# xab1315_df_a_ev_1 = np.square(xab1315_df_a_ev_1)
# xab1315_df_a_ev_2 = np.square(xab1315_df_a_ev_2)
# xk1787_df_a_ev_2 = np.square(xk1787_df_a_ev)


#xk1787_df_a_ev_onecol = single_col_fun(xk1787_df_a_ev, '297')

# xk1787_df_a_ev_onecol.plot(kind= 'line', color = 'black')
# plt.yscale('log')
# plt.xlabel('Energy eV')
# plt.ylabel('Absorption Coefficient Squared')
# plt.title('Single column plotter')

#gaas_df_av_ev = ev_converter_calc(gaas_df_av,1e-6)

sample_regression_dict, egap_dict = linearfit(xab1315_df_a_ev_2, xab1315_params_dict)
# = ev_converter_calc(xab1315_df_norm, 1e-6)

xk1787_regression_dict, egap_xk1787 = linearfit(xk1787_df_a_ev_2, xk1787_params_dict)

# R O L L I N G   A V E R A G E R 
# xab1315_r_020223 = rolling_averager(xab13     15_df_a_ev_1, 10000)
# xab1315_r_080323 = rolling_averager(xab1315_df_a_ev_2, 10000)
xab1315_r_020223 = xab1315_df_a_ev_1.rolling(30).mean()
xab1315_r_020223.dropna(inplace = True)

xab1315_r_080323 = xab1315_df_a_ev_2.rolling(30).mean()
xk1787_r = xk1787_df_a_ev_2.rolling(400).mean()
xab1315_deriv_1 = deriv_calc(xab1315_r_080323, xab1315_custom_range)
print(egap_xk1787)
xk1787_deriv = deriv_calc(xk1787_r, xk1787_custom_range)
#xab1315_df_norm_ev = xab1315_df_norm_ev.set_index('eV')
#gaas_df_av = gaas_df_av.drop(columns= ['eV'])


# NOTE talk to laura bout this part 

xkd_lim = [0.6, 0.67]

xk1787_bandgap = maximumvaluefinder(xk1787_deriv, xkd_lim)
#print(xk1787_bandgap)
# Convert data to two lists to be processed correctly

xk1787_t_data = list(xk1787_bandgap.index)
xk1787_e_data = list(xk1787_bandgap.values)
print(xk1787_e_data)
print(xk1787_t_data)
# curvefit on xk1787
xk1787_params, xk1787_cov = varshni_fit(xk1787_t_data, xk1787_e_data)


egap_t_plot(
    xk1787_params,
    xk1787_e_data,
    xk1787_t_data
            )

plt.show()

# plt.figure(3)
# egap_plot(
#     xk1787_bandgap, 'Bandgap vs T for XK1787 0.05 Indium', 
#     'Temperature (K)', 
#     'Band Gap E_g (eV)')

# raw_plot(
#     gaas_020223_av,
#     'GaAs Sub 020223',
#     'Wavelength $\mu$m', 
#     'Transmission Fraction',
#     colour_1, 
#     colour_2
# ) 
# plt.figure(1)
# raw_plot(
#     gaas_080223_av,
#     'GaAs Sub 080223',
#     'Wavelength $\mu$m', 
#     'Transmission Fraction',
#     colour_1, 
#     colour_2
# ) 
# plt.figure(1)
# raw_plot(
#     xab1315_df_norm_ev,
#     'XAB1315 T, Normalized with GaAs Sub',
#     'Photon Energy (eV)', 
#     'SSC',
#     colour_1, 
#     colour_2
# )
# plt.figure(2)
# raw_plot(
#     xk1787_df_a_ev,
#     'XK1787 T Alpha',
#     'Photon Energy(eV)', 
#     'alpha',
#     colour_1, 
#     colour_2
# ),
# plt.yscale('log')

# a_plot(
#     xab1315_r_020223,
#     'XAB1315 T, subsrate cube backround 020223',
#     'Photon Energy (eV)', 
#     'alpha**2',
#     colour_1, 
#     colour_2
# )
# plt.figure(1)
# a_plot(
#     xab1315_r_080323,
#     'XAB1315 T, subsrate cryostat backround 080223',
#     'Photon Energy (eV)', 
#     'alpha**2',
#     colour_1, 
#     colour_2
# )
# plt.figure(1)
# a_plot(
#     xk1787_df_a_ev_2,
#     'XK1787 T Alpha',
#     'Photon Energy(eV)', 
#     r'$\alpha^{2}$',
#     colour_1, 
#     colour_2
# )
# #print(xab1315_deriv)
# plt.figure(2)
# raw_plot(
#     xk1787_deriv,
#     'XK1787 Derivative Plot rolling mean 250',
#     'Photon Energy (eV)',
#     'derivate',
#     colour_1,
#     colour_2
# )
# plt.xlim(0.5, 0.75)
# plt.show()

