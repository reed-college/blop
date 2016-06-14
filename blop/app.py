from flask import Flask, render_template
from blop import db
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = db.db_url

db = SQLAlchemy(app)


@app.route('/login/')
def login():
    return render_template('signin.html')


@app.route('/submit')
def submit():
    return render_template('submit.html')


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


if __name__ == '__main__':
    app.run()
