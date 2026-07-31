import pandas as pd


def verify_extension(path: str) -> bool:
    """Check for extension in filename, only csv"""
    file_extension = ["csv"]

    if '.' in path:
        # [-1] = the last element in the list.
        if path.split(".")[-1] in file_extension:
            return True
        else:
            print("Error: wrong extension: only '.csv' authorized")
            return False
    # no '.' in the filename, so no extension.
    else:
        print("Error: invalid filename: no extension")
        return False


# return type is DataFrame, it's a class.
def load(path: str) -> pd.DataFrame:
    """Return a DataFrame from a .csv"""
    try:
        if verify_extension(path) is False:
            return None
        df = pd.read_csv(path)
        if df.empty:
            print("Error : DataFrame is empty")
            return None
        # print(f"Loading dataset of dimension : {df.shape}")

    except Exception as error:
        print(f"Error : {error}")
        return None
    return df
