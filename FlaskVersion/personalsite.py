#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 17:29:59 2021

@author: user
"""

from flask import Flask, render_template, url_for
app = Flask(__name__)

# morse_to_english = #code here
# english_to_morse = #code here
# core4 = #code here

# nanmageddon = #file route here
# biopatch = #file route here
# transcendence = #file route here

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/projects")
def projects():
    return render_template("morse.html")

@app.route("/projects/morse")
def morse():
    return render_template("morse.html")
    
@app.route("/projects/core4")
def core4():
    return render_template("core4.html")
        
@app.route("/stories")
def stories():
    return render_template("stories.html")
        
@app.route("/stories/Nanmageddon")
def nanmageddon():
    return render_template("nanmageddon.html")

@app.route("/stories/biopatch")
def biopatch():
    return render_template()

@app.route("/stories/transcendence")
def transcendence():
    return render_template()

if __name__ == '__main__':
    app.run(debug=True)