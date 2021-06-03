"""Server for landlord review app."""

from flask import (Flask, render_template, request, flash, session,
                    redirect)
from model import connect_to_db
# import crud <-- un-comment afer crud.py complete
from jinja2 import StrictUndefined
import os

app = Flask(__name__)
app.secret_key = os.environ['secret_key']
app.jinja_env.undefined = StrictUndefined

# @app.route('/')
# def render_homepage():

#     return render_template('homepage.html')
# <-- un comment after creating homepage.html