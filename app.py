#app.py
from flask import Flask, request, render_template
import urllib
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.dates import date2num

from io import BytesIO

import pandas as pd
from datetime import datetime, timedelta


# %matplotlib inline
from mpl_finance import candlestick_ohlc
from pandas.plotting import register_matplotlib_converters


app = Flask(__name__)

df = pd.read_csv("BTC-USD.csv", index_col = 0, parse_dates=True)
fig, ax = plt.subplots(1,1)
ax.plot(df["Open"])

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/myplot")
def myplot():
    return render_template("myplot.html")

@app.route("/plot/btc")
def plot_btc():

    # Obtain query parameters
    start = datetime.strptime(request.args.get("start", default="2017-12-1", type=str), "%Y-%m-%d")
    end = datetime.strptime(request.args.get("end", default="2017-12-31", type=str), "%Y-%m-%d")

    if start > end:
        start, end = end, start
    if (start + timedelta(days=7)) > end:
        end = start + timedelta(days=7)

    png_out = BytesIO()

    ax.set_xlim([start, end])
    ax.set_ylabel("USD/BTC")

    plt.xticks(rotation=30)

    plt.savefig(png_out, format="png", bbox_inches="tight")
    img_data = urllib.parse.quote(png_out.getvalue())

    return "data:image/png:base64," + img_data

@app.route("/living_cost")
def living_cost():
    print("#lllllllllll")
    register_matplotlib_converters()
    fig = plt.figure(figsize=(20,10))
    ax = fig.add_subplot(2,2,1)
    ax2 = fig.add_subplot(2,2,2)
    ax3 = fig.add_subplot(2,2,3)
    ax4 = fig.add_subplot(2,2,4)

    df = pd.read_csv("spending_part1.csv", index_col = 0, parse_dates=True)
    spending = df["消費支出"].copy()
    exept_home = df["消費支出(除く住居等※)"].copy()
    food = df["食料"].copy()
    medical = df["保健医療"].copy()
    traffic = df["交通・通信"].copy()
    education = df["教育"].copy()
    ent = df["教養娯楽"].copy()
    cloths = df["被服及び履物"].copy()
    home = df["住居"].copy()
    for i, v in enumerate(food):
        if v != v:
            continue
        spending[i] = int(spending[i].replace(",", ""))
        home[i] = int(home[i].replace(",", ""))
        exept_home[i] = int(exept_home[i].replace(",", ""))
        food[i] = int(food[i].replace(",", ""))
        medical[i] = int(medical[i].replace(",", ""))
        traffic[i] = int(traffic[i].replace(",", ""))
        education[i] = int(education[i].replace(",", ""))
        ent[i] = int(ent[i].replace(",", ""))
        cloths[i] = int(cloths[i].replace(",", ""))

    ax.plot(spending, label="Total")
    ax.plot(exept_home, label="Except Home")

    ax2.plot(traffic, label="Traffic")
    ax2.plot(ent, label="Entertainment")
    ax3.plot(food, label="Food")
    ax4.plot(home, label="Home")
    ax4.plot(medical, label="Medical")
    ax4.plot(education, label="Education")
    ax4.plot(cloths, label="Cloths")

    plt.title("Graph Title")
    plt.xlabel("year/month")
    plt.ylabel("YEN")
    plt.legend()
    ax.set_xlim(["2017/2", "2019/1"])

    png_out = BytesIO()

    # ax.set_xlim([start, end])
    # ax.set_ylabel("USD/BTC")

    plt.xticks(rotation=30)

    plt.savefig(png_out, format="png", bbox_inches="tight")
    img_data = urllib.parse.quote(png_out.getvalue())

    print("#lllllllllllllllllllllkkkkkkkkkkkkkkkkkkklll")

    return "data:image/png:base64," + img_data

if __name__ == "__main__":
    app.run(debug=True, port=5000)
