from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd

def projection_life(data1 : pd.DataFrame, data2 : pd.DataFrame):

    # print("gross dom product :\n", data1)
    # print("life expect :\n", data2)
    xgraph = data1['1900']
    ygraph = data2['1900']
    plt.title('1900')
    plt.ylabel("Life Expectancy")
    plt.xlabel("Gross domestic product")
    plt.scatter(xgraph, ygraph)
    plt.xscale('log')
    # plt.xticks(date[1::40])
    plt.xticks([300, 1000, 10000],['300','1K', '10K'])
    plt.show()

if __name__ == '__main__':

    data1 = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    data2 = load("life_expectancy_years.csv")
    projection_life(data1, data2)