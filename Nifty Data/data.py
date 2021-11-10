import pandas as pd
import json

# API Key
# Go ahead use it... play with it... I don't mind
KEY = 347896


def fetch_nifty_index_data(index: str):
    indices = {
        "50": "Nifty50",
        "auto": "NiftyAuto",
        "bank": "NiftyBank",
        "it": "NiftyIT",
        "pharma": "NiftyPharma"
    }
    sheetName = indices[index.lower()]
    sheetId = "1FaSibXFWRJ8bFoOIEy4vaoxG7z-S8nUhT6U9f4quvaU"
    base_url = f"https://docs.google.com/spreadsheets/d/{sheetId}/gviz/tq?tqx=out:csv&sheet={sheetName}"
    # print(base_url)
    data = pd.read_csv(base_url)
    data["TICKER"] = data["SYMBOL"]
    data.set_index("SYMBOL", inplace=True)
    # print(data.head(11))
    jsonData = data.to_json(orient="index")
    return json.loads(jsonData)


if __name__ == "__main__":
    print(fetch_nifty_index_data("auto"))
