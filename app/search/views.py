from flask import Flask, Blueprint, render_template
from app import app

mod = Blueprint('search', __name__)

@mod.route('/search/')
def search():
	return render_template('search/search.html')