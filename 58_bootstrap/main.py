from flask import Flask, render_templates
import datetime

@app.route('/')
def home():
    
    current_year = datetime.datetime.now().year
    return render_template("index.html", year = current_year)