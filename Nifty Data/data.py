import pandas as pd
import json

# API Key
# Go ahead use it... play with it... I don't mind
KEY = 347896


def fetch_nifty_50_data():
    sheetId = "1FaSibXFWRJ8bFoOIEy4vaoxG7z-S8nUhT6U9f4quvaU"
    sheetName = "Nifty50"
    base_url = f"https://docs.google.com/spreadsheets/d/{sheetId}/gviz/tq?tqx=out:csv&sheet={sheetName}"
    # print(base_url)
    data = pd.read_csv(base_url, index_col="SYMBOL")
    # print(data.head(11))
    jsonData = data.to_json(orient="index")
    return json.loads(jsonData)


def fetch_nifty_bank_data():
    sheetId = "1FaSibXFWRJ8bFoOIEy4vaoxG7z-S8nUhT6U9f4quvaU"
    sheetName = "NiftyBank"
    base_url = f"https://docs.google.com/spreadsheets/d/{sheetId}/gviz/tq?tqx=out:csv&sheet={sheetName}"
    # print(base_url)
    data = pd.read_csv(base_url, index_col="SYMBOL")
    # print(data.head(11))
    jsonData = data.to_json(orient="index")
    return json.loads(jsonData)


def fetch_nifty_it_data():
    sheetId = "1FaSibXFWRJ8bFoOIEy4vaoxG7z-S8nUhT6U9f4quvaU"
    sheetName = "NiftyIT"
    base_url = f"https://docs.google.com/spreadsheets/d/{sheetId}/gviz/tq?tqx=out:csv&sheet={sheetName}"
    # print(base_url)
    data = pd.read_csv(base_url, index_col="SYMBOL")
    # print(data.head(11))
    jsonData = data.to_json(orient="index")
    return json.loads(jsonData)


if __name__ == "__main__":
    print(fetch_nifty_bank_data())
