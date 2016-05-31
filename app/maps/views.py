from flask import Flask, Blueprint, render_template
from app import app

mod = Blueprint('maps', __name__)

@mod.route('/')
@mod.route('/map')
def maps():
	return render_template('map/map.html')