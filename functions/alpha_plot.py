from matplotlib import pyplot as plt 
from functions.base_importer import basic_importer
from functions.colours.colour_gradient import get_color_gradient
def a_plot(
    df,
    title,
    xlabel,
    ylabel, 
    color1,
    color2
):
    """
    This function plots the absorption coefficient with a logarithmic yaxis 
    Args:
        df:             pd.DataFrame; Dataframe from file importer
        title:          str; title for the graph
        substrate_path: str; path of substrate data to import 
        xlabel:         str; label we want to put on the x-axis
        ylabel:         str; label we want to put on the y-axis
    """
    # Clear the values 
    col_0 = []
    col_1 = []

    df.plot(kind = 'line', color = get_color_gradient(color1, color2, len(df.columns)))
    plt.legend()
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    #plt.yscale('log')

