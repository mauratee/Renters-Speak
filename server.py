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
    """Show all reviews by calling get_reviews function"""
    reviews = crud.get_reviews()

    return render_template('all_reviews.html', reviews=reviews)


@app.route('/landlords')
def all_landlords():
    """Show all reviews by calling get_landlords function"""
    landlords = crud.get_landlords()

    return render_template('all_landlords.html', landlords=landlords)


@app.route('/buildings')
def all_buildings():
    """Show all buildings by calling get_buildings function"""
    buildings = crud.get_buildings()

    return render_template('all_buildings.html', buildings=buildings)


@app.route('/users', methods=['POST'])
def register_user():
    """Create a new user"""
    



if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)