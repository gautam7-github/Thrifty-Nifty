from flask import Flask, Response, jsonify
from flask_ngrok import run_with_ngrok
from data import *
import pyperclip

# config
app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True

# using ngrok's free deployment tunnels to test this API
run_with_ngrok(app)

# home route


@app.route("/")
def home():
    pyperclip.copy(f"/{KEY}/nifty/50/data/all")
    return f"/{KEY}/data/nifty/index/all"


@app.route(f"/{KEY}/data/nifty/<index>/all")
def send_nifty_index_data(index):
    indices = {
        'it': fetch_nifty_it_data(),
        'bank': fetch_nifty_bank_data(),
        '50': fetch_nifty_50_data()
    }
    if index in indices:
        return jsonify(indices[index])


if __name__ == "__main__":
    app.run()
