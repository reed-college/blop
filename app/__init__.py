import os
from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object('config')

from app.auth.views import mod as authModule
app.register_blueprint(authModule)

from app.search.views import mod as searchModule
app.register_blueprint(searchModule)

from app.blotter.views import mod as blotterModule
app.register_blueprint(blotterModule)

from app.maps.views import mod as mapModule
app.register_blueprint(mapModule)