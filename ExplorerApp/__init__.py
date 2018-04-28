#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 13:35:55 2018

@author: maadland
"""
import os
import numpy as np 
import pandas as pd 
from flask import Flask, request, render_template
import pandas_profiling as pp
app = Flask(__name__)

@app.route("/")
def form():
    """Renders a form to upload
    """
    return render_template("explorer_upload.html")

@app.route("/transform", methods=["GET", "POST"])
def display():
    data_type = str(request.form.get("select"))
    raw_file = request.files["data_file"]
    raw = pd.read_csv(raw_file, encoding="latin1")
    profile = pp.ProfileReport(raw)
    return profile.to_html()
    # return raw.head(100).to_html()

if __name__ == "__main__":
    # data = pd.read_csv("sample.csv", encoding="latin1")
    # raw = data 
    app.run(debug=True)
