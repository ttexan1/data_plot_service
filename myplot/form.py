from myplot import app
from flask import Flask, request, render_template, make_response, jsonify
import werkzeug
import urllib
import numpy as np
import os
import matplotlib.pyplot as plt
from io import BytesIO
import csv
plt.rcParams["font.family"] = "IPAexGothic"

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

@app.route("/files/index")
def file_index():
    import glob
    fp = os_file_path()
    paths = glob.glob(fp+"/*")
    names = []
    for p in paths:
        name = p.split("/")[len(p.split("/"))-1]
        names.append(name)
    return make_response(jsonify({'result': names}))
