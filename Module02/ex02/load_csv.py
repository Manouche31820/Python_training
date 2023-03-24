import pandas as pd


def load(path: str) -> pd.DataFrame:

    try:
        data = pd.read_csv(path)
        return data
    except FileNotFoundError:
        print("File do not exists.")
    except UnicodeDecodeError:
        print("Bad format :", path)
    except Exception:
        print("Error")