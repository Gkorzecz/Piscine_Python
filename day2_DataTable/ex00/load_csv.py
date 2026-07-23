import pandas as pd

# return type is DataFrame, it's a class.
def load(path: str) -> pd.DataFrame:
    """Return a DataFrame from a .csv"""
    try:
        df = pd.read_csv(path)
        # if df.empty:
        #     print("Error : DataFrame is empty")
        #     return None
        print(f"Loading dataset of dimension : {df.shape}")

    except Exception as error:
        print(f"Error : {error}")
        return None
    return df


def main():
    print("\033[1mSubject Test :\033[0m")
    print(load("life_expectancy_years.csv"))
    print()

    print("\033[1mWrong extension (.png) :\033[0m")
    print(load("wrong_extension.png"))
    print()

    print("\033[1mNo extension :\033[0m")
    print(load("no_extension"))
    print()

    print("\033[1mDoes not exist :\033[0m")
    print(load("does_not_exist.csv"))
    print()

    print("\033[1mEmpty:\033[0m")
    print(load("empty_data.csv"))
    print()


if __name__ == "__main__":
    main()
