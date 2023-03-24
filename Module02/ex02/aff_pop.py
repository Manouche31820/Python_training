from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd

def aff_pop(data : pd.DataFrame):

    date = list(data.head(0))
    data2 = data[data["country"].str.contains("France")]
    data3 = data[data["country"].str.contains("Belgium")]
    int_array2 = [int(float(s[:-1]) * 1000000) for s in data2.values[0][1:]]
    int_array3 = [int(float(s[:-1]) * 1000000) for s in data3.values[0][1:]]
    plt.title('Population Projections')
    plt.ylabel("Population")
    plt.xlabel("Year")
    plt.plot(date[1:], int_array3, label="Belgium", c = "blue")
    plt.plot(date[1:], int_array2, label="France", c = "green")
    plt.legend(loc='lower right')
    plt.xticks(date[1::40])
    plt.yticks([20000000, 40000000, 60000000],['20M', '40M', '60M'])
    plt.show()

if __name__ == '__main__':

    data = load("population_total.csv").iloc[:, :252]
    aff_pop(data)