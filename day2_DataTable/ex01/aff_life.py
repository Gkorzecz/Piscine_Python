import matplotlib.pyplot as plt
from load_csv import load


def main():
    """Load a dataset, and show life expectancy projections for France"""
    data = load("life_expectancy_years.csv")

    france = data[data["country"] == "France"]

    years = data.columns[1:].astype(int)
    life_expectancy = france.iloc[0, 1:]

    plt.plot(years, life_expectancy)

    # Show one tick every 40 years
    plt.xticks(range(years.min(), years.max(), 40))

    plt.title("France Life expectancy Projections")
    plt.ylabel("Life expectancy")
    plt.xlabel("Year")
    plt.show()


if __name__ == "__main__":
    main()
