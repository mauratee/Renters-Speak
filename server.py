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


@app.route('/buildings/<building_id>')
def show_building(building_id):
    """Show details of a particular building"""

    building = crud.get_building_by_id(building_id)

    return render_template('building_details.html', building=building)


@app.route('/all_users')
def all_users():
    """Show all users by calling get_users function."""

    users = crud.get_users()

    return render_template('all_users.html', users=users)


@app.route('/users', methods=['POST'])
def register_user():
    """Create a new user"""
    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)

    if user:
        flash("""Can't create account. Account with this email already
               exists. Please try again.""")
    else:
        crud.create_user(email, password)
        flash("Account created successfully! Please log in.")
    
    return redirect("/")


@app.route('/login', methods=['POST'])
def login():
    """Allow existing users to log in"""

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email_and_password(email, password)

    if user:
        session["user_email"] = user.email
        flash(f"Welcome back, {user.email}! You are now logged in.")
    else:
        flash("Please enter correct email and password or register for new account.")

    return redirect('/')


@app.route('/write_review', methods=['POST'])
def write_review():
    """If user logged in, allow submission from write review form on homepage.html
         to be added to reviews database"""
    
    logged_in_email = session.get("user_email")
    reviewed_landlord = request.form.get("landlord")
    reviewed_building = request.form.get("building")
    written_review = request.form.get("review_body")

    if logged_in_email is None:
        flash("You must log in to review a landlord.")
    else:
        user = crud.get_user_by_email(logged_in_email)
        # building = 
        # created_on = 
        # updated_at = 
        review_body = written_review



    return redirect('/reviews')


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)