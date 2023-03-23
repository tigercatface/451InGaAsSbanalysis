import numpy as np 


def res_data_creator(
        res_dict,
        sample_limits_dict,
):
    data_dict = {}

    for sample in res_dict:
        results = 0
        lowlim= 0
        highlim = 0
        x = 0
        y = 0
        lowlim = sample_limits_dict[sample][0]
        highlim = sample_limits_dict[sample][1]
        results = res_dict[sample]

        uppylim = highlim* results.slope + results.intercept + 5e7
        y = np.linspace(0, uppylim, 50)
        x = (y-results.intercept)/results.slope

        data_dict[sample] = [x,y]
        # y = mx + c
    return(data_dict)
        
