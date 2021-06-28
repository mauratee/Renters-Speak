"""Server for landlord review app."""

from flask import (Flask, render_template, request, flash, session,
                    redirect, jsonify)
from model import connect_to_db
import crud
from jinja2 import StrictUndefined
import os
import requests

app = Flask(__name__)
app.secret_key = os.environ['secret_key']
app.jinja_env.undefined = StrictUndefined


####### Routes for Rendering HTML Pages

@app.route('/')
def render_homepage():

    return render_template('homepage.html')


@app.route('/user_login')
def render_login():

    return render_template('login.html')

@app.route('/write_review')
def render_write_reviews():

    return render_template('write_review.html')

@app.route('/new_user')
def render_new_user():

    return render_template('new_user.html')


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

@app.route("/new_user", methods=['POST'])
def register_user():
    """Create a new user"""
   
    email = request.form.get("email")
    username = request.form.get("username")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    get_username = crud.get_user_by_username(username)

    if user:
        flash(u"""Can't create account. Account with this email already
               exists. Please try again.""", "error")
        return redirect("/new_user")
    elif get_username:
        flash (u"""Account with this username already exists. Please enter 
        another username and try again.""", "error")
        return redirect("/new_user")
    else:
        crud.create_user(email, username, password)
        flash(u"Account created! Please log in.", "success")
        return redirect("/user_login")


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
        flash(f"Welcome back, {user.username}. You are now logged in.", "success")
        return "None"
    else:
        return "Please enter correct email and password or register for a new account."


@app.route("/logout")
def logout():
    """Allow currently logged in user to log out"""
    
    if "user_id" in session and "user_email" in session:
        del session["user_id"]
        del session["user_email"]
        flash(u"You are now logged out.", "success")
        return redirect('/user_login')
    else:
        flash(u"You are not currently logged in.", "error")
        return redirect('/user_login')
    
    


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
        flash(u"You must log in to review a landlord.", "error")
        return redirect('/user_login')
    elif not reviewed_landlord:
        flash(u"You didn't enter the Landlord for your review.", "error")
    elif not reviewed_building:
        flash(u"You didn't enter the Address for your review.", "error")
    elif not written_review:
        flash(u"You didn't enter the Review Text for your review.", "error")
    else:
        user = crud.get_user_by_email(logged_in_email)

        # Pass reviewed building address to NYC Geosearch API to return
        # housenumber, street and postalcode variables
        url = "https://geosearch.planninglabs.nyc/v1/autocomplete"
        payload = {"text": reviewed_building}
        res = requests.get(url, params=payload)
        data = res.json()
        features = data["features"]
        properties = features[0]["properties"]

        housenumber = properties["housenumber"]
        streetname = properties["street"]
        postalcode = properties["postalcode"]

        building = crud.get_building_by_address(housenumber, 
                                                streetname, 
                                                postalcode)
        landlord = crud.get_landlord_by_name(reviewed_landlord)

        # If both not in database, create landlord and building entries
        # in respective databases
        if not building and not landlord:
            landlord = crud.create_landlord(reviewed_landlord, landlord_office)
            building = crud.create_building(housenumber, streetname, 
                                            postalcode, landlord.landlord_id)
        elif not building and landlord:
            building = crud.create_building(housenumber, streetname, 
                                            postalcode, landlord.landlord_id)
        elif not landlord and building:
            landlord = crud.create_landlord(reviewed_landlord, landlord_office)

        
        crud.create_review(written_review, user, building)

        flash(f"""You wrote a review of {building.building_housenumber} {building.building_streetname}.
                     Thanks for your review submission!""", "success")

    return redirect('/reviews')


####### Routes for Search

@app.route("/search_address")
def search_nyc_address():
    """Takes in user input from html form and makes API call to NYC Geosearch
        based on user input. Then passes API response to crud function to
        check if entry exists in database. If exists, return details page
        for that building."""

    text = request.args.get("search_nyc_address")

    if text is None:
        flash(u"You must enter an address to search.", "error")
        return redirect('/')

    url = "https://geosearch.planninglabs.nyc/v1/autocomplete"
    payload = {"text": text}
    res = requests.get(url, params=payload)
    data = res.json()
    features = data["features"]
    properties = features[0]["properties"]

    searched_housenumber = properties["housenumber"]
    searched_streetname = properties["street"]
    searched_postalcode = properties["postalcode"]

    building = crud.get_building_by_address(searched_housenumber, searched_streetname, searched_postalcode)
    violation_list = crud.get_violation_by_address(searched_housenumber, searched_streetname,
                                                 searched_postalcode)
    registrations = crud.get_hpdregistration_by_address(searched_housenumber, searched_streetname,
                                                            searched_postalcode)
    contacts = []
    if registrations:
        for registration in registrations:
            contact = crud.get_hpdcontact_by_registration(registration.registrationid)
            contacts.append(contact)
    print("!!!!!!!!!!!!!!!!!!!!!")
    print(f"contacts = {contacts}")

    if contacts:
        contact_list = contacts[0]
    print("!!!!!!!!!!!!!!!!!!!!!")
    print(f"contact_list = {contact_list}")

    
    violations = {}
    for violation in violation_list:
        if violation.violation_class in violations:
            violations[violation.violation_class] +=1
        else:
            violations[violation.violation_class] = 1
    
    violation_counts = list(violations.values())
    print("~~~~~~~~~~~~~~~~~~~")
    print(violation_counts)
    violation_types = list(violations.keys())
    print("~~~~~~~~~~~~~~~~~~~")
    print(violation_types)


    # data = '{"labels":' + f'{violation_types}' + ', "datasets":[{"data":' + f'{violation_counts}' + '}]}'
    data = '{"labels":["A", "C", "B"], "datasets":[{"data":' + f'{violation_counts}' + ', "backgroundColor":["#3e309c", "#b8b1e7", "#3819e6"] }]}'

    print("!!!!!!!!!!!!!!!!!!!!!")
    print(data)
    #"datasets":[{"data":[2, 4, 8]}]
    # "labels":["does", "this", "work"],

    

    if building is None and not violation_list:
        flash(u"No reviews or violations exist for that address.", "error")
        return redirect('/')

    elif building is None and violation_list:
        length_violation_list = len(violation_list)
        return render_template("violation_details.html", violation_list=violation_list,
                                length_violation_list=length_violation_list)
                                # Add data=data if rendering chart.js in violation_details.html

    elif not violation_list and building:
        return render_template('building_details.html', building=building, 
                                violation_list=violation_list)
        

    length_violation_list = len(violation_list)
    return render_template('building_details.html', building=building, 
                            violation_list=violation_list, length_violation_list=length_violation_list, 
                            data=data, registrations=registrations, contact_list=contact_list)



@app.route("/search_by_address")
def search_by_building_and_violation():
    """Takes in user input from html form and passes to crud function to
        check if entry exists in database. If exists, return details page
        for that building."""

    searched_housenumber = request.args.get("search_review_by_housenumber")
    searched_streetname = request.args.get("search_review_by_streetname")
    searched_postalcode = request.args.get("search_review_by_postalcode")

    if searched_housenumber is None or searched_streetname is None or searched_postalcode is None:
        flash(u"You must enter a complete address to search.", "error")
        return redirect('/')
    else:
        building = crud.get_building_by_address(searched_housenumber, searched_streetname, searched_postalcode)
        violation_list = crud.get_violation_by_address(searched_housenumber, searched_streetname,
                                                 searched_postalcode)


        if building is None and not violation_list:
            flash("No reviews or violations exist for that address.")
            return redirect('/')

        elif building is None and violation_list:
            length_violation_list = len(violation_list)
            return render_template("violation_details.html", violation_list=violation_list,
                                length_violation_list=length_violation_list)

        elif not violation_list and building:
            return render_template('building_details.html', building=building, 
                                    violation_list=violation_list)
        

        length_violation_list = len(violation_list)
        return render_template('building_details.html', building=building, 
                                violation_list=violation_list, length_violation_list=length_violation_list)


@app.route("/search_by_landlord")
def search_by_landlord():
    """Takes in user input from html form, passes to crud function to check
    if exists in database. If exists, return details page for that landlord."""

    searched_landlord = request.args.get("search_landlord")
    # print(f"searched_landlord = {searched_landlord}")

    if searched_landlord is None:
        flash(u"You must enter a landlord to search.", "error")
        return redirect('/')
    else:
        landlord = crud.get_landlord_by_name(searched_landlord)

        if landlord is None:
            flash("No reviews exist for that landlord.")
            return redirect("/")
        
        return render_template("landlord_details.html", landlord=landlord)


@app.route("/search_hpdviolations_by_address")
def search_violations_by_address():
    """Takes in user input from html form, breaks into house number, street name,
        and postal code and then queries hpd_violations database. If address exists
        in database, return associated violation objects."""

    searched_housenumber = request.args.get("search_hpd_by_housenumber")
    searched_streetname = request.args.get("search_hpd_by_streetname")
    searched_postalcode = request.args.get("search_hpd_by_postalcode")

    if searched_housenumber is None or searched_streetname is None or searched_postalcode is None:
        flash(u"You must enter a complete address to search.", "error")
        return redirect('/')
    else:
        violation_list = crud.get_violation_by_address(searched_housenumber, searched_streetname,
                                                 searched_postalcode)
        length_violation_list = len(violation_list)

        if violation_list is None:
            flash("No violations exist for that address.")
            return redirect("/")
        
        return render_template("violation_details.html", violation_list=violation_list,
                                length_violation_list=length_violation_list)


####### Routes for Autocomplete

@app.route("/autocomplete")
def autocomplete():
    """Get list of 10 matching addresses for any given user input."""

    search = request.args.get('q')

    url = "https://geosearch.planninglabs.nyc/v1/autocomplete"
    payload = {"text": search}
    res = requests.get(url, params=payload)
    data = res.json()
    features = data["features"]
    first_ten = features[0:9]
    # print("!!!!!!!!!!")
    # print(f"first_ten = {first_ten}")

    address_list = []

    for location in first_ten:
        address_list.append(location["properties"]["label"])

    print("!!!!!!!!!!")
    print(f"address_list = {address_list}")
    
    return jsonify(matching_results=address_list)

    # return address_list




if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)