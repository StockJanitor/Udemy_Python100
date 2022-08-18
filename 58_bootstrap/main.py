from flask import Flask, render_templates
import datetime
app = Flask()

@app.route('/')
def home():
    
    current_year = datetime.datetime.now().year
    return render_templates("index.html", year = current_year)