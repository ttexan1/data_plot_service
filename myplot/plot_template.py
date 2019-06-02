from myplot import app
from flask import Flask, request, render_template, make_response, jsonify
import urllib
import os
import matplotlib.pyplot as plt
from io import BytesIO
import csv
plt.rcParams["font.family"] = "IPAexGothic"

import pandas as pd
from mpl_finance import candlestick_ohlc
from pandas.plotting import register_matplotlib_converters

def os_file_path():
    fp = os.getenv("UPLOAD_DIR_PATH")
    if fp == "" or fp == None:
        fp = "/Users/higashitetsuji/Desktop/OCS2019/12-flask-02-ttexan1/myplot/csv"
    return fp

@app.route("/plot/free")
def display_plot():
    return render_template("plot_template.html")

@app.route("/plot/parameters")
def parameters():
    name = request.args.get('file_name')
    fp = os_file_path()
    csv_file = open(fp+"/"+name, "r", encoding="utf-8", errors="", newline="" )
    f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
    headers = next(f)
    return make_response(jsonify({'result': headers}))

@app.route("/plot/data")
def plot_data():
    name = request.args.get('file_name')
    fp = os_file_path()
    csv_file = open(fp+"/"+name, "r", encoding="utf-8", errors="", newline="" )
    f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
    headers = next(f)
    df = pd.read_csv("myplot/csv/"+name, parse_dates=True)
    fig, ax = plt.subplots(1,1)
    for header in headers:
        if header == headers[0]:
            ax.set_xticklabels(df[header],rotation=60)
            continue
        if request.args.get(header, type=str) == "true":
            prepared_data = []
            for raw in df[header]:
                prepared_data.append(float(raw))
            ax.plot(prepared_data, label=header)
    ax.legend()
    ax.set_ylabel(name)
    plt.xticks(rotation=30)
    png_out = BytesIO()
    plt.savefig(png_out, format="png", bbox_inches="tight")
    img_data = urllib.parse.quote(png_out.getvalue())

    return "data:image/png:base64," + img_data
