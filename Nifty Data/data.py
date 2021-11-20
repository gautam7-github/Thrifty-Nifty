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
        "pharma": "NiftyPharma",
        "fmcg": "NiftyFMCG"
    }
    sortcodes = {
        "alph": "SYMBOL",
        "price": "CMP",
        "mcap": "MKTCAP",
        "chng": "CHANGEPCT"
    }
    sheetName = indices[index.lower()]
    sheetId = "1FaSibXFWRJ8bFoOIEy4vaoxG7z-S8nUhT6U9f4quvaU"
    base_url = f"https://docs.google.com/spreadsheets/d/{sheetId}/gviz/tq?tqx=out:csv&sheet={sheetName}"
    data = pd.read_csv(base_url)
    data["TICKER"] = data["SYMBOL"]
    if sortBy in ["alph"]:
        ascend = True
    else:
        ascend = False
    data.sort_values(by=sortcodes[sortBy], ascending=ascend, inplace=True)
    data.set_index("SYMBOL", inplace=True)
    jsonData = data.to_json(orient="index")
    return json.loads(jsonData)


def fetch_all_indices_data():
    sheetName = "Indices"
    sheetId = "1FaSibXFWRJ8bFoOIEy4vaoxG7z-S8nUhT6U9f4quvaU"
    base_url = f"https://docs.google.com/spreadsheets/d/{sheetId}/gviz/tq?tqx=out:csv&sheet={sheetName}"
    data = pd.read_csv(base_url)
    data.set_index("SYMBOL", inplace=True)
    jsonData = data.to_json(orient="index")
    return json.loads(jsonData)


if __name__ == "__main__":
    print(fetch_all_indices_data())
