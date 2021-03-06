from flask import Flask, jsonify
from flask.templating import render_template
from threading import Thread
from data import *

# config
app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True


# home route
@app.route("/")
def home():
    return render_template("index.html")

# f"/{KEY}/data/nifty/index/all/sort/sortby"


@app.route("/help")
def help():
    return render_template("help.html")

# index route


@app.route(f"/{KEY}/data/nifty/<string:index>/all/sort/<string:sortby>")
def send_nifty_index_data(index, sortby):
    index = str(index).lower()
    sortby = str(sortby).lower()
    indices = {
        'it': fetch_nifty_index_data("it", sortby),
        'bank': fetch_nifty_index_data("bank", sortby),
        '50': fetch_nifty_index_data("50", sortby),
        'auto': fetch_nifty_index_data("auto", sortby),
        'pharma': fetch_nifty_index_data("pharma", sortby),
        'fmcg': fetch_nifty_index_data("fmcg", sortby)
    }
    if index in indices:
        return jsonify(indices[index])

# all index route


@app.route(f"/{KEY}/data/nifty/indices/all")
def send_all_nifty_indices_data():
    return jsonify(fetch_all_indices_data())


def run():
    app.run(host='0.0.0.0', port=8080)


def main():
    t = Thread(target=run)
    t.start()


if __name__ == "__main__":
    main()
