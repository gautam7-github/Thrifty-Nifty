from flask import Flask, Response, jsonify
from flask.templating import render_template
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
    return render_template("index.html")


@app.route("/help")
def help():
    return f"/{KEY}/data/nifty/index/all/sort/sortby"

# index route


@app.route(f"/{KEY}/data/nifty/<index>/all/sort/<sortby>")
def send_nifty_index_data(index, sortby):
    index = str(index).lower()
    indices = {
        'it': fetch_nifty_index_data("it", sortby),
        'bank': fetch_nifty_index_data("bank", sortby),
        '50': fetch_nifty_index_data("50", sortby),
        'auto': fetch_nifty_index_data("auto", sortby),
        'pharma': fetch_nifty_index_data("pharma", sortby)
    }
    if index in indices:
        return jsonify(indices[index])


if __name__ == "__main__":
    app.run()
