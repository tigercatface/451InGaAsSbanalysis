from functions.folder_importer2 import folder_importer_os
from functions.raw_plotter import raw_plot
from matplotlib import pyplot as plt 
A = 5
plt.rc('figure', figsize=[46.82 * .5**(.5 * A), 33.11 * .5**(.5 * A)])

#plt.rc('text', usetex=True)
plt.rc('font', family='serif')
colour_1 = "#0dd9cb"
colour_2 = "#6e0202"
folder_path_5 = 'data/091122_bg'

df1 = folder_importer_os(folder_path_5)

df2 = df1[['XAB1308','XAB1309']]
df2['XAB1308 Correctedgit '] = df1['XAB1308'].apply(lambda x: x*10)

df3 = df1.divide(df1['GaAs'], axis  = 0)
df2['XAB1309 Normalized'] = df3['XAB1309']
df2 = df2[df2.index > 1.5]
df2 = df2[df2.index < 5]
# raw_plot(
#     df2,
#     'Transmission for Single and Double Side Polished Samples', 
#     r'Wavelength ($\mu$m)', 
#     'Transmission Fraction', colour_1, colour_2)
df2.plot(kind = 'line')
plt.legend()
plt.title('Transmission for Single and Double Side Polished Samples')
plt.ylabel('Transmisison (fraction)')
plt.xlabel(r'Wavelength ($\mu$m)')
plt.show()