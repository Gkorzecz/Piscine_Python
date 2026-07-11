import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from load_csv import load


def convert_population(value):
    value = str(value)

    if value.endswith("M"):
        return float(value[:-1]) * 1_000_000

    return float(value)


def millions_formatter(value, position):
    return f"{int(value / 1_000_000)}M"


def main():
    """Load a dataset, and show population for France and Belgium."""
    data = load("population_total.csv")

    france = data[data["country"] == "France"]
    belgium = data[data["country"] == "Belgium"]

    years = data.columns[1:252].astype(int)

    population_france = france.iloc[0, 1:252].apply(convert_population)
    population_belgium = belgium.iloc[0, 1:252].apply(convert_population)

    plt.plot(years, population_belgium, label="Belgium")
    plt.plot(years, population_france, label="France")

    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")

    plt.xticks(range(1800, 2050, 40))
    plt.gca().yaxis.set_major_formatter(FuncFormatter(millions_formatter))

    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
