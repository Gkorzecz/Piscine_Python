import matplotlib.pyplot as plt
from load_csv import load


def main():
    """Display life expectancy according to GDP in 1900."""
    income = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life = load("life_expectancy_years.csv")

    plt.scatter(income["1900"], life["1900"])

    plt.title("1900")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life expectancy")

    # Usually expected for this exercise
    plt.xscale("log")
    plt.xticks([300, 1000, 10000], ["300", "1k", "10k"])
    plt.show()


if __name__ == "__main__":
    main()
