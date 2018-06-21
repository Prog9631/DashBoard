#graphs

def plot_graph():
    import matplotlib.pyplot as plt
    import readsheet_functions as rsf
    import reading_excel_sheet as res
    import parameter_dictionary_PAC as PAC

    y = rsf.get_col(res.file,res.sheet,PAC.Parameter1S[3])
    x = range(1,len(y)+1)

    # plotting the points 
    plt.plot(x, y)
     
    # naming the x axis
    plt.xlabel('production (tonns)')
    # naming the y axis
    plt.ylabel('days')
     
    # giving a title to my graph
    plt.title('PAC production')
     
    # function to show the plot
    plt.show()

plot_graph()
