from myplot import app
from flask import Flask, request, render_template, make_response, jsonify
import werkzeug
import urllib
import numpy as np
import os
import matplotlib.pyplot as plt
from matplotlib.dates import date2num

from io import BytesIO

import pandas as pd
from datetime import datetime, timedelta
from mpl_finance import candlestick_ohlc
from pandas.plotting import register_matplotlib_converters

def os_file_path():
    fp = os.getenv("UPLOAD_DIR_PATH")
    if fp == "" or fp == None:
        fp = "/Users/higashitetsuji/Desktop/OCS2019/12-flask-02-ttexan1/myplot/csv"
    return fp

@app.route("/csv_form")
def csv_form():
    return render_template("form.html")

@app.route("/csv_form_submit", methods=["POST"])
def csv_form_submit():
    UPLOAD_DIR = os_file_path()
    file = request.files['uploadFile']
    fileName = file.filename
    if '' == fileName:
        make_response(jsonify({'result':'filename must not empty.'}))
    saveFileName = datetime.now().strftime("%Y%m%d_%H%M%S_") \
        + werkzeug.utils.secure_filename(fileName)
    file.save(os.path.join(UPLOAD_DIR, saveFileName))
    return make_response(jsonify({'result':'upload OK.'}))
    # return render_template("form.html")

@app.route("/files/index")
def file_index():
    import glob
    fp = os_file_path()
    paths = glob.glob(fp+"/*")
    names = []
    for p in paths:
        name = p.split("/")[len(p.split("/"))-1]
        names.append(name)
    print(names)
    return make_response(jsonify({'result': names}))

@app.route("/plot/free")
def display_plot():
    return render_template("plot_template.html")


@app.route("/plot/data")
def plot_data():
    name = request.args.get('file_name')
    # TODO: ユーザーのデータをプロットするのを完了する。
    # TODO: 余計なimport moduleを削除する
    df = pd.read_csv("myplot/csv/BTC-USD.csv", index_col = 0, parse_dates=True)
    fig, ax = plt.subplots(1,1)
    ax.plot(df["Open"])
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
