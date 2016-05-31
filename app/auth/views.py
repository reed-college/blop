from flask import Flask, Blueprint, render_template
from app import app

mod = Blueprint('auth', __name__)

@mod.route('/login/')
def login():
	return render_template('auth/signin.html')