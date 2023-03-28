import numpy as np 
import pandas as pd
from functions.derivativecalc import deriv_calc
from matplotlib import pyplot as plt

derivative_ranges_dict = {
    'XAB1315': [0.45,0.476],
    'XAB1308': [0.494,0.520],
    'XAB1309': [0.544,0.586],
    'XK1786' : [0.573,0.606],
    'XK1787' : [0.63,0.681]
    }

df = pd.read_pickle('091122_data')
df = np.sqrt(df)
dfrolled = df.rolling(500).mean()
dfderoved = deriv_calc(dfrolled, [0.45, 0.7])
maximal_deriv_locations = {}
for columns in dfderoved.columns:
    penis_gap = 0
    dfsection  = dfderoved.copy()
    dfsection = dfsection[dfsection.index > derivative_ranges_dict[columns][0]]
    dfsection = dfsection[dfsection.index < derivative_ranges_dict[columns][1]]
    penis_gap = dfsection[columns].idxmax()
    print(columns, ' maximum in derivative is', penis_gap, 'eV')
    maximal_deriv_locations[columns]  = penis_gap


# SECTION 2: Error time: 
#   1. Create a delta df of abs diff between dfrolled and df 
#   2. square
#   3. rolling(500)
#   4. sqrt(df)
#   5. sub in my values and see what the error is at m iloc locations 

error_df = df - dfrolled
error_df2 = np.square(error_df)
error_dfr = error_df2.rolling(500).mean()
error_rmse = np.sqrt(error_dfr)

for sample in error_rmse:
    mean_error = 0
    errorsection = error_rmse.copy()
    errorsection = errorsection[errorsection.index > derivative_ranges_dict[sample][0]]
    errorsection = errorsection[errorsection.index < derivative_ranges_dict[sample][1]]
    mean_error = errorsection[sample].iloc[int(maximal_deriv_locations[sample])]
    print(sample, 'Mean RMSE error is ', mean_error, 'eV')
# dfderoved.plot()
# plt.show()
