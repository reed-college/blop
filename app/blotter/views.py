from flask import Flask, Blueprint, render_template
from app import app

mod = Blueprint('blotter', __name__, url_prefix='/blotter')

@mod.route('/submit')
def submit():
	return render_template('/blotter/submit.html')

@mod.route('/blotter')
def blotter():
	return render_template('/blotter/blotter.html')