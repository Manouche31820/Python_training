from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd

def aff_life(data : pd.DataFrame):

    date = list(data.head(0))
    data2 = data[data["country"].str.contains("France")]
    plt.title('France Life expectancy Projections')
    plt.ylabel("Life expectancy")
    plt.xlabel("Year")
    plt.plot(date[1:], data2.values[0][1:])
    plt.xticks(date[1::40])
    plt.show()

if __name__ == '__main__':

    data = load("life_expectancy_years.csv")
    aff_life(data)