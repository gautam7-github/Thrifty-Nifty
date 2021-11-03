import pandas as pd
import json

# API Key
KEY = 347896


def fetch_nifty_50_data():
    sheetId = "1FaSibXFWRJ8bFoOIEy4vaoxG7z-S8nUhT6U9f4quvaU"
    sheetName = "Nifty50"
    base_url = f"https://docs.google.com/spreadsheets/d/{sheetId}/gviz/tq?tqx=out:csv&sheet={sheetName}"
    # print(base_url)
    data = pd.read_csv(base_url, index_col="SYMBOL")
    jsonData = data.to_json(orient="index")
    return json.loads(jsonData)


if __name__ == "__main__":
    print(fetch_nifty_50_data())
