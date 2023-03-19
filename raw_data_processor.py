from functions.folder_importer2 import folder_importer_os
from functions.raw_plotter import raw_plot
from matplotlib import pyplot as plt 



folder_path_1 = 'data/071122_bg'
folder_path_2 = 'data/071122_bg/backroundall'
folder_path_3 = 'data/071122_bg/other' # Many index errors, manual forced plotting leads to same as the rest
folder_path_4 = 'data/031122_bg'
folder_path_5 = 'data/091122_bg'
folder_path_6 = 'data/091122_2_bg'
folder_path_7 = 'data/251022_bg'

df1 = folder_importer_os(folder_path_1)
df2 = folder_importer_os(folder_path_2)
df4 = folder_importer_os(folder_path_4)
df5 = folder_importer_os(folder_path_5)
df6 = folder_importer_os(folder_path_6)
df7 = folder_importer_os(folder_path_7)

plt.figure(0)
raw_plot(
    df1,
    '071122 Raw Data',
    '$\mu m$',
    'SSC')

plt.figure(1)
raw_plot(
    df2,
    '071122 Raw Data Backroundall',
    '$\mu m$',
    'SSC'
)
plt.figure(2)
raw_plot(
    df4,
    '031122 Raw Data',
    '$\mu m$',
    'SSC'
)
plt.figure(3)
raw_plot(
    df5,
    '091122',
    '$\mu m$',
    'SSC'
)
plt.figure(4)
raw_plot(
    df6,
    '091122_2',
    '$\mu m$',
    'SSC'
)
plt.figure(5)
raw_plot(
    df7,
    '251022',
    '$nm $',
    'SSC'
)
plt.show()
