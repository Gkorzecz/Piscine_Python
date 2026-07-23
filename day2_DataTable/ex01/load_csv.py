import pandas as pd


# return type is DataFrame, it's a class.
def load(path: str) -> pd.DataFrame:
    """Return a DataFrame from a .csv"""
    try:
        df = pd.read_csv(path)
        # print(f"Loading dataset of dimension : {df.shape}")

    except Exception as error:
        print(f"Error : {error}")
        return None
    return df