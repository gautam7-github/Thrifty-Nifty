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
    return f"/{KEY}/data/nifty/50/all"

# nifty 50 route


@app.route(f"/{KEY}/data/nifty/50/all")
def fetch_nifty50_data():
    return jsonify(fetch_nifty_50_data())

# nifty bank route


@app.route(f"/{KEY}/data/nifty/bank/all")
def fetch_niftybank_data():
    return jsonify(fetch_nifty_bank_data())


if __name__ == "__main__":
    app.run()
