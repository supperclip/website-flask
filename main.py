from flask import Flask

from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config["SECRET_KEY"] = "buh"
app.config["WTF_CSRF_ENABLED"] = False

@app.route("/")
def index():
    return render_template("base.html")

@app.route("/a")
def a():
    return render_template("layer1.html")

@app.route("/ULTRAKILL")
def ULTRAKILL():
    return render_template("layer1.html")

@app.route("/DOOM")
def DOOM():
    return render_template("layer1.html")

@app.route("/AmidEvil")
def AmidEvil():
    return render_template("layer1.html")

app.run(host='0.0.0.0', port=5001)