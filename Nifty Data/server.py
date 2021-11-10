from flask import Flask, Response, jsonify
from flask_ngrok import run_with_ngrok
from data import *

# config
app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True

# using ngrok's free deployment tunnels to test this API
run_with_ngrok(app)

# home route


@app.route("/")
def home():
    return f"/{KEY}/data/nifty/index/all"

# index route


@app.route(f"/{KEY}/data/nifty/<index>/all")
def send_nifty_index_data(index):
    index = str(index).lower()
    indices = {
        'it': fetch_nifty_index_data("it"),
        'bank': fetch_nifty_index_data("bank"),
        '50': fetch_nifty_index_data("50"),
        'auto': fetch_nifty_index_data("auto"),
        'pharma': fetch_nifty_index_data("pharma")
    }
    if index in indices:
        return jsonify(indices[index])


if __name__ == "__main__":
    app.run()
