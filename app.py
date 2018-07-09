#app.py
from flask import Flask, request, render_template
import urllib
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.dates import date2num

from io import BytesIO

import pandas as pd
from datetime import datetime

app = Flask(__name__)

df = pd.read_csv("BTC-USD.csv", index_col = 0, parse_dates=True)
fig, ax = plt.subplots(1,1)
ax.plot(df["Open"])

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/plot/btc")
def exec_calculate():

    # Obtain query parameters
    start = request.args.get("start", default="2017-12-1", type=str)
    end = request.args.get("end", default="2018-4-1", type=str)
    
    png_out = BytesIO()

    ax.set_xlim([start, end])
    ax.set_ylabel("USD/BTC")

    plt.xticks(rotation=30)

    plt.savefig(png_out, format="png", bbox_inches="tight")
    img_data = urllib.parse.quote(png_out.getvalue())

    return "data:image/png:base64," + img_data

if __name__ == "__main__":
    app.run(debug=True, port=5000)
