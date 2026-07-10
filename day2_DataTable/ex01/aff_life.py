import matplotlib.pyplot as plt
from load_csv import load


def main():
    """Load a dataset, and show """
    data = load("life_expectancy_years.csv")

    # select the row designed "France"
    france = data[data["country"] == "France"]
    # print(france)

    years = data.columns[1:]
    life_expectancy = france.iloc[0, 1:]
    # print(life_expectancy)

    plt.plot(years, life_expectancy)
    plt.title("France Life expectancy Projections")
    plt.ylabel("Life expectancy")
    plt.xlabel("Year")
    plt.show()


if __name__ == "__main__":
    main()