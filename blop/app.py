from flask import Flask, render_template, request
from blop import db
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = db.db_url

db = SQLAlchemy(app)

from blop import models


@app.route('/login/')
def login():
    return render_template('signin.html')


@app.route('/submit', methods=['GET', 'POST'])
def submit():

    types = models.Type.query.all()
    locations = models.Location.query.all()

    return render_template('submit.html', types=types, locations=locations)


@app.route('/blotter')
def blotter():
    return render_template('blotter.html')


@app.route('/')
@app.route('/map')
def maps():
    return render_template('map.html')


@app.route('/search/')
def search():
    return render_template('search.html')


@app.route('/processform', methods=['GET', 'POST'])
def processform():
    # This is for testing.
    # Put the database interactions for the form here.
    f = request.form
    codelist = []
    for key in f.keys():
        for value in f.getlist(key):
            codelist.append(value)
    return "Incident type(s):  " + str(codelist)
    types = []
    incident_code = request.form['incident dropdown']
    types.append(incident_code)

    location = request.form['']

    datetime = request.form['']

    incident_summary = request.form['incident summary']

    incident = models.Incident(
                               datetime=datetime,
                               summary=incident_summary,
                               location=location,
                               types=types
                               )
    db.session.add(incident)
    db.session.commit()

    return "The incident type is " + str(incident_code)


if __name__ == '__main__':
    app.run()
