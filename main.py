from flask import Flask

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()

app.config["SECRET_KEY"] = "buh"
app.config["WTF_CSRF_ENABLED"] = False

class timeDatabase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timeData = db.Column(db.Integer, index=True)
    runnerData = db.Column(db.String(80), index=True)
    timeStringValue = db.Column(db.String(80), index=True)
    __table_args__ = (
        db.UniqueConstraint('timeData', 'runnerData', name='uix_time_runner'),
    )

class doomTimeDatabase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timeData = db.Column(db.Integer, index=True)
    runnerData = db.Column(db.String(80), index=True)
    timeStringValue = db.Column(db.String(80), index=True)
    __table_args__ = (
        db.UniqueConstraint('timeData', 'runnerData', name='uix_time_runner'),
    )

class amidEviltimeDatabase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timeData = db.Column(db.Integer, index=True)
    runnerData = db.Column(db.String(80), index=True)
    timeStringValue = db.Column(db.String(80), index=True)
    __table_args__ = (
        db.UniqueConstraint('timeData', 'runnerData', name='uix_time_runner'),
    )

class timeValueInput(FlaskForm):
    givenTimeInput = StringField("Please enter the time value:", validators=[DataRequired()])
    runnerName = StringField("Please enter the username of the runner:", validators=[DataRequired()])
    submit_knop = SubmitField("Submit")

def translateStringToSeconds(timeInput):
    time_parts = timeInput.split(':')
    if len(time_parts) != 3:
        return False
    h, m, s = time_parts
    try:
        h = int(h)
        m = int(m)
        s = int(s)
        if (s > 60) or (m > 60):
            return False
        total_seconds = (h * 3600) + (m * 60) + s
        return total_seconds
    except ValueError:
        return False

db.create_all()

ultrakillData = None
doomData = None
amidEvilData = None

@app.route("/ULTRAKILL", methods=["GET", "POST"])
def ULTRAKILL():
    inputForm = timeValueInput()
    if inputForm.validate_on_submit():
        timeValue = inputForm.givenTimeInput.data
        runnerNameData = inputForm.runnerName.data
        timeString = inputForm.givenTimeInput.data
        existing_entry = timeDatabase.query.filter_by(timeData=translateStringToSeconds(timeValue), runnerData=runnerNameData).first()
        if existing_entry:
            pass
        else:
            timeValueInSeconds = translateStringToSeconds(timeValue)
            if timeValueInSeconds:
                new_entry = timeDatabase(timeData=timeValueInSeconds, timeStringValue=timeString, runnerData=runnerNameData)
                try:
                    db.session.add(new_entry)
                    db.session.commit()
                except IntegrityError:
                    db.session.rollback()
    
    # Order the entries by timeData (in seconds) from low to high
    ultrakillData = timeDatabase.query.order_by(timeDatabase.timeData.asc()).all()
    return render_template("layer1.html", data=ultrakillData, template_form=inputForm)


@app.route("/DOOM", methods=["GET", "POST"])
def DOOM():
    inputForm = timeValueInput()
    if inputForm.validate_on_submit():
        timeValue = inputForm.givenTimeInput.data
        runnerNameData = inputForm.runnerName.data
        timeString = inputForm.givenTimeInput.data
        existing_entry = doomTimeDatabase.query.filter_by(timeData=translateStringToSeconds(timeValue), runnerData=runnerNameData).first()
        if existing_entry:
            pass
        else:
            timeValueInSeconds = translateStringToSeconds(timeValue)
            if timeValueInSeconds:
                new_entry = doomTimeDatabase(timeData=timeValueInSeconds, timeStringValue=timeString, runnerData=runnerNameData)
                try:
                    db.session.add(new_entry)
                    db.session.commit()
                except IntegrityError:
                    db.session.rollback()
    
    # Order the entries by timeData (in seconds) from low to high
    doomData = doomTimeDatabase.query.order_by(doomTimeDatabase.timeData.asc()).all()
    return render_template("layer1.html", data=doomData, template_form=inputForm)

@app.route("/AmidEvil", methods=["GET", "POST"])
def AmidEvil():
    inputForm = timeValueInput()
    if inputForm.validate_on_submit():
        timeValue = inputForm.givenTimeInput.data
        runnerNameData = inputForm.runnerName.data
        timeString = inputForm.givenTimeInput.data
        existing_entry = amidEviltimeDatabase.query.filter_by(timeData=translateStringToSeconds(timeValue), runnerData=runnerNameData).first()
        if existing_entry:
            pass
        else:
            timeValueInSeconds = translateStringToSeconds(timeValue)
            if timeValueInSeconds:
                new_entry = amidEviltimeDatabase(timeData=timeValueInSeconds, timeStringValue=timeString, runnerData=runnerNameData)
                try:
                    db.session.add(new_entry)
                    db.session.commit()
                except IntegrityError:
                    db.session.rollback()
    
    # Order the entries by timeData (in seconds) from low to high
    amidEvilData = amidEviltimeDatabase.query.order_by(amidEviltimeDatabase.timeData.asc()).all()
    return render_template("layer1.html", data=amidEvilData, template_form=inputForm)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("homePage.html")

app.run(host='0.0.0.0', port=5001)