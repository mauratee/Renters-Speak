"""Server for landlord review app."""

from flask import (Flask, render_template, request, flash, session,
                    redirect)
from model import connect_to_db
import crud
from jinja2 import StrictUndefined
import os

app = Flask(__name__)
app.secret_key = os.environ['secret_key']
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def render_homepage():

    return render_template('homepage.html')


@app.route('/reviews')
def all_reviews():

    return render_template('all_reviews.html')


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)