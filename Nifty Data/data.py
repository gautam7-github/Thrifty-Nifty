import pandas as pd
import json

# API Key
# Go ahead use it... play with it... I don't mind
KEY = 347896


def fetch_nifty_index_data(index: str, sortBy: str):
    indices = {
        "50": "Nifty50",
        "auto": "NiftyAuto",
        "bank": "NiftyBank",
        "it": "NiftyIT",
        "pharma": "NiftyPharma"
    }
    sortcodes = {
        "alph": "SYMBOL",
        "price": "CMP"
    }
    sheetName = indices[index.lower()]
    sheetId = "1FaSibXFWRJ8bFoOIEy4vaoxG7z-S8nUhT6U9f4quvaU"
    base_url = f"https://docs.google.com/spreadsheets/d/{sheetId}/gviz/tq?tqx=out:csv&sheet={sheetName}"
    data = pd.read_csv(base_url)
    data["TICKER"] = data["SYMBOL"]
    data.sort_values(by=sortBy, ascending=False, inplace=True)
    data.set_index("SYMBOL", inplace=True)
    jsonData = data.to_json(orient="index")
    return json.loads(jsonData)


if __name__ == "__main__":
    print(fetch_nifty_index_data("Auto"))
