from datetime import datetime
from flask import Flask, render_template, request, redirect
from flask.helpers import url_for
import requests as r
import json as j
from requests.api import get

app = Flask(__name__)

@app.route('/')
def index():
    Title = "HomePage"
    Time = str(datetime.now())
    return render_template("index.html",title=Title, time=Time)

@app.route('/about')
def about():
    Title = "About"
    Time = str(datetime.now())
    return render_template("about.html",title=Title, time=Time)

@app.route('/contact')
def contact():
    Title = "Contact"
    Time = str(datetime.now())
    return render_template("Contact.html",title=Title, time=Time)

@app.route('/time')
def Time():
    Title = "Time"
    Time = str(datetime.now())
    return render_template("time.html",title=Title, time=Time)

@app.route('/weather', methods = ["GET", "POST"])
def Weather():
    Title = "Weather"
    if request.method == 'POST':
        city = request.form.get('cty')
        Wtr_temp = r.get(f"https://goweather.herokuapp.com/weather/{city}")
        WeatherDict = j.loads(Wtr_temp.text)
        temper = WeatherDict['temperature']
        descript = WeatherDict['description']
        return redirect(url_for('display_weather', temperature=temper, description=descript))
    return render_template("weather.html",title=Title)

@app.route('/display_weather')
def display_weather():
    Title = "Weather"
    temper = request.args.get("temperature", None)
    descript = request.args.get("description", None)
    return render_template("display_weather.html",title=Title, temperature=temper, description=descript)
