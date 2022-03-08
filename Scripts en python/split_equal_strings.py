import numpy as np
import matplotlib.pyplot as plt

def split_equal_strings(data,substrings):
    split_data = np.array([])
    k = len(data)//substrings
    for i in range(0,len(data),k):
        if(len(data[i:i+k])==k):
            split_data = np.append(split_data,data[i:i+k])
    return split_data

def percentage_analysis(split_array, nucleotide):
    perc_data = np.array([])
    x_axis_array = np.array([])

    for i in range(0,len(split_array)):
        long = len(split_array[i])
        coun = split_array[i].count(nucleotide)
        perc = coun*100/long
        perc_data = np.append(perc_data,perc)
        x_axis_array = np.append(x_axis_array,i)
    return perc_data, x_axis_array

def cytosine_guanine_graphic(c_graph_data,g_graph_data, a_graph_data, t_graph_data, x_axis,ref_perc):

    c_bars_data = np.array([])
    for i in range(0,len(c_graph_data)):
        c_bars_data = np.append(c_bars_data,c_graph_data[i]-ref_perc)

    g_bars_data = np.array([])
    for i in range(0,len(g_graph_data)):
        g_bars_data = np.append(g_bars_data,g_graph_data[i]-ref_perc)

    a_bars_data = np.array([])
    for i in range(0,len(a_graph_data)):
        a_bars_data = np.append(a_bars_data,a_graph_data[i]-ref_perc)

    t_bars_data = np.array([])
    for i in range(0,len(t_graph_data)):
        t_bars_data = np.append(t_bars_data,t_graph_data[i]-ref_perc)


    plt.subplot(3,2,1)
    plt.scatter(x_axis, c_graph_data)
    plt.axhline(y=ref_perc, color='r', linestyle='-')
    plt.bar(x_axis, c_bars_data, width=0.4, bottom=ref_perc)
    plt.ylabel('% Cytosine')
    plt.xlabel('Genome Position')
    plt.grid()
    plt.plot()

    plt.subplot(3,2,3)
    plt.scatter(x_axis, g_graph_data)
    plt.axhline(y=ref_perc, color='r', linestyle='-')
    plt.bar(x_axis, g_bars_data, width=0.3, bottom=ref_perc)
    plt.ylabel('% Guanine')
    plt.xlabel('Genome Position')
    plt.grid()
    plt.plot()

    plt.subplot(3,2,5)
    plt.scatter(x_axis, g_graph_data - c_graph_data)
    plt.bar(x_axis, g_bars_data - c_bars_data, width=0.3)
    plt.ylabel('Frequency of Guanine - Cytosine')
    plt.xlabel('Genome Position')
    plt.grid()
    plt.plot()




    plt.subplot(3,2,2)
    plt.scatter(x_axis, a_graph_data)
    plt.axhline(y=ref_perc, color='r', linestyle='-')
    plt.bar(x_axis, a_bars_data, width=0.4, bottom=ref_perc)
    plt.ylabel('% Adenine')
    plt.xlabel('Genome Position')
    plt.grid()
    plt.plot()

    plt.subplot(3,2,4)
    plt.scatter(x_axis, t_graph_data)
    plt.axhline(y=ref_perc, color='r', linestyle='-')
    plt.bar(x_axis, t_bars_data, width=0.3, bottom=ref_perc)
    plt.ylabel('% Thymine')
    plt.xlabel('Genome Position')
    plt.grid()
    plt.plot()

    plt.subplot(3,2,6)
    plt.scatter(x_axis, a_graph_data - t_graph_data)
    plt.bar(x_axis, a_bars_data - t_bars_data, width=0.3)
    plt.ylabel('Frequency of Adenine - Thymine')
    plt.xlabel('Genome Position')
    plt.grid()
    plt.plot()

    plt.suptitle("Yersinia_pestis")
    plt.show()


def main():
    filename = "Datasets/E_coli.txt"
    #filename = "Datasets/Vibrio_cholerae.txt"
    #filename = "Datasets/Escherichia_coli.txt"
    #filename = "Datasets/Yersinia_pestis.txt"
    with open(filename, 'r') as file:
        data = file.read()

    print(len(data))
    substrings = 500
    split_data = split_equal_strings(data,substrings)
    c_split_percent, x_axis = percentage_analysis(split_data, "C")
    g_split_percent, x_axis = percentage_analysis(split_data, "G")
    a_split_percent, x_axis = percentage_analysis(split_data, "A")
    t_split_percent, x_axis = percentage_analysis(split_data, "T")

    cytosine_guanine_graphic(c_split_percent,g_split_percent,a_split_percent,t_split_percent,x_axis,25)

if __name__=="__main__":
    main()
