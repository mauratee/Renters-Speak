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


####### Routes for Viewing All Entries for each DB Class

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


@app.route('/users')
def all_users():
    """Show all users by calling get_users function."""

    users = crud.get_users()

    return render_template('all_users.html', users=users)


####### Routes for Viewing Individual Entry for each DB Class

@app.route('/buildings/<building_id>')
def show_building(building_id):
    """Show details of a particular building"""

    building = crud.get_building_by_id(building_id)

    return render_template('building_details.html', building=building)


@app.route('/landlords/<landlord_id>')
def show_landlord(landlord_id):
    """Show details of a particular landlord"""

    landlord = crud.get_landlord_by_id(landlord_id)

    return render_template('landlord_details.html', landlord=landlord)


@app.route('/users/<user_id>')
def show_user(user_id):
    """Show details of a particular user"""

    user = crud.get_user_by_id(user_id)

    return render_template('user_details.html', user=user)


@app.route('/reviews/<review_id>')
def show_review(review_id):
    """Show details of a particular review"""

    review = crud.get_review_by_id(review_id)

    return render_template('review_details.html', review=review)


####### Routes for User Creation

@app.route('/new_user', methods=['POST'])
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


####### Routes for Login/Logout

@app.route("/login", methods=["POST"])
def login():
    """Allow existing users to log in"""

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email_and_password(email, password)
 
    if user:
        session["user_email"] = user.email
        session["user_id"] = user.user_id
        flash(f"Welcome back, {user.email}! You are now logged in.")
    else:
        flash("Please enter correct email and password or register for new account.")


    return redirect("/")


@app.route("/logout")
def logout():
    """Allow currently logged in user to log out"""

    print("~"*10)
    print(session)
    
    if session:
        session.pop("user_id")
        session.pop("user_email")
        print("*"*15)
        print(session)
        flash(f"You are now logged out.")
    else:
        flash("You are not currently logged in.")
    
    return redirect('/')


####### Routes for Reviews

@app.route('/write_review', methods=['POST'])
def write_review():
    """If user logged in, allow submission from write review form on homepage.html
         to be added to reviews database"""
    
    logged_in_email = session.get("user_email")

    reviewed_landlord = request.form.get("landlord")
    reviewed_building = request.form.get("building")
    written_review = request.form.get("review_body")
    landlord_office = request.form.get("landlord_office")

    if logged_in_email is None:
        flash("You must log in to review a landlord.")
    elif not reviewed_landlord:
        flash("Error: you didn't enter the Landlord for your review.")
    elif not reviewed_building:
        flash("Error: you didn't enter the Building for your review.")
    elif not written_review:
        flash("Error: you didn't enter the Review Text for your review.")
    else:
        user = crud.get_user_by_email(logged_in_email)
        building = crud.get_building_by_address(reviewed_building)
        landlord = crud.get_landlord_by_name(reviewed_landlord)

        # Check if reviewed building and reviewed landlord in database.
        # If both not in database, create landlord and building entries
        # in respective databases
        if not building and not landlord:
            landlord = crud.create_landlord(reviewed_landlord, landlord_office)
            building = crud.create_building(reviewed_building, landlord.landlord_id)

        crud.create_review(written_review, user, building)

        flash(f"You wrote a review for {landlord.landlord_name} who owns {building.building_address}.")

    return redirect('/reviews')


####### Routes for Search

@app.route("/search_by_address")

@app.route("/search_by_landlord")
def search_by_landlord():
    """Takes in user input from html form, passes to crud function to check
    if exists in database. If exists, return ddetails page for that landlord."""

    searched_landlord = request.form.get("search_landlord")

    if searched_landlord is None:
        flash("You must enter a landlord to search.")
    else:
        landlord = crud.get_landlord_by_name(searched_landlord)
    
        if not landlord:
            flash("No reviews exist for that landlord.")

        return render_template('landlord_details.html', landlord=landlord)



if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)