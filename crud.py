"""CRUD operations for landlord review site"""

import datetime
from model import db, User, Landlord, Building, Review, HPDViolation, HPDRegistration, HPDContact, connect_to_db


# || Functions for API Calls ||

# def geosearch_api(text):
#     return properties

def hpd_violations_api(searched_housenumber, searched_streetname, searched_postalcode):

    # Transform string to match data format in DB
    searched_streetname = searched_streetname.upper()

    url = "https://data.cityofnewyork.us/resource/wvxf-dwi5.json"
    payload = {"housenumber": searched_housenumber, "streetname": searched_streetname, 
              "zip": searched_postalcode}
    res = requests.get(url, params=payload)
    data = res.json()

####### Functions for Database Entry Creation

def create_user(email, username, password):
    """Create and return a new user."""

    user = User(email=email, username=username, password=password)

    db.session.add(user)
    db.session.commit()

    return user


def create_landlord(landlord_name, office_address):
    """Create and return a new landlord."""

    landlord = Landlord(landlord_name=landlord_name, office_address=office_address)

    db.session.add(landlord)
    db.session.commit()

    return landlord


def create_building(building_housenumber, building_streetname, building_postcode, landlord_id):
    """Create and return a new building."""

    building = Building(building_housenumber=building_housenumber, building_streetname=building_streetname,
                        building_postcode=building_postcode, landlord_id=landlord_id)

    db.session.add(building)
    db.session.commit()

    return building


def create_review(review_body, user, building):
    """Create and return a new review."""

    review = Review(review_body=review_body, user=user,
                    building=building)
    
    db.session.add(review)
    db.session.commit()

    return review


####### Functions to Get All Entries in Database

def get_reviews():
    """View all reviews in reviews table"""

    return Review.query.all()


def get_landlords():
    """View all landlords in landlords table"""

    return Landlord.query.all()


def get_buildings():
    """View all landlords in landlords table"""

    return Building.query.all()


def get_users():
    """Query users table and return all users"""

    return User.query.all()


####### Functions to Get a Specifc Entry in Database (if it exists!)

def get_review_by_id(review_id):
    """Takes in review id as argument and checks if review exists in "reviews"
        database. If review exists, returns review object. If review does not
        exist, returns None."""

    return Review.query.filter(Review.review_id == review_id).first()


def get_building_by_id(building_id):
    """Takes in building id as argument and checks if building exists in "buildings"
        database. If building exists, returns building object. If building does not
        exist, returns None."""
    
    return Building.query.filter(Building.building_id == building_id).first()


def get_building_by_address(housenumber, streetname, postcode):
    """Takes in building address as argument and checks if building exists in "buildings"
        database. If building exists, returns building object. If building does not
        exist, returns None."""

    return Building.query.filter(Building.building_housenumber == housenumber,
                                    Building.building_streetname ==streetname,
                                    Building.building_postcode == postcode).first()


def get_landlord_by_id(landlord_id):
    """Takes in landlord id as argument and checks if landlord exists in "landlords"
        database. If landlord exists, returns landlord object. If landlord does not
        exist, returns None."""
    
    return Landlord.query.filter(Landlord.landlord_id == landlord_id).first()


def get_landlord_by_name(landlord_name):
    """Takes in landlord name as argument and checks if landlord exists in "landlords"
        database. If landlord exists, returns landlord object. If landlord does not
        exist, returns None."""
    
    # Creates f string based on argument, adding % to format for .like Query
    landlord_name = (f"%{landlord_name}%")

    return Landlord.query.filter(Landlord.landlord_name.like(landlord_name)).first()


def get_user_by_id(user_id):
    """Takes in user id and checks if user exists in "users" database.
        If user exists, return user object. If user does not exist, return None."""

    return User.query.filter(User.user_id == user_id).first()


def get_user_by_email(email):
    """Takes in email address and checks if email exists in "users" database.
        If user exists, return user object. If user does not exist, return None."""
    
    return User.query.filter(User.email == email).first()


def get_user_by_username(username):
    """Takes in username and checks if username exists in "users" database.
        If username exists, return associated user object. If username does 
        not exist, return None."""

    return User.query.filter(User.username == username).first()


def get_user_by_email_and_password(email, password):
    """Takes in email and password and checkes if email exists in "users" database.
        If email exists, check if password matches password in database for that user. 
        If email does not exist in database, return None.  If email exists, but password
        does not match, return None."""
    
    user = User.query.filter(User.email == email).first()

    if user:
        if user.password == password:
            return user
    else:
        return None


def get_violation_by_address(housenumber, streetname, postcode):
    """Takes in house number, streetname and postcode and returns all entries in
        HPDViolation class that match all parameters"""

    # Transform string to match data format in DB
    streetname = streetname.upper()

    return HPDViolation.query.filter(HPDViolation.housenumber == housenumber,
                                    HPDViolation.streetname ==streetname,
                                    HPDViolation.postcode == postcode).all()


def get_hpdviolation_by_address(building):
    """Takes in building object and returns HPDViolation object that matches building"""

    housenumber = building.building_housenumber
    streetname = building.building_streetname
    postalcode = building.building_postcode

    return HPDViolation.query.filter(HPDViolation.housenumber == housenumber,
                                    HPDViolation.streetname ==streetname,
                                    HPDViolation.postcode == postcode).one()


def get_hpdregistration_by_address(housenumber, streetname, postcode):
    """Takes in house number, streetname and postcode and returns all entries in
        HPDRegistration class that match all parameters. Uses registrations to query
        HPDContact class and returns all contact options matching registrationid
        in registrations."""


    return HPDRegistration.query.filter(HPDRegistration.housenumber == housenumber,
                                    HPDRegistration.streetname ==streetname,
                                    HPDRegistration.postcode == postcode).all()


def get_hpdcontact_by_registration(registrationid):
    """Takes in house number, streetname and postcode and returns all entries in
        HPDRegistration class that match all parameters. Uses registrations to query
        HPDContact class and returns all contact options matching registrationid
        in registrations."""


    return HPDContact.query.filter(HPDContact.registrationid == registrationid).all()


####### Functions to Query NYC Geosearch API

def get_nyc_geosearch_results(text):
    """Takes in text and returns list of first 10 address labels that 
        match text from NYC Geosearch API"""

    url = "https://geosearch.planninglabs.nyc/v1/autocomplete"
    payload = {"text": text}
    res = requests.get(url, params=payload)
    data = res.json()
    features = data["features"]
    first_ten = features[0:9]
    labels_list = []

    for location in first_ten:
        labels_list.append(location["label"])

    print("!!!!!!!!!!")
    print(f"labels_list = {labels_list}")
    return labels_list




if __name__ == '__main__':
    from server import app
    connect_to_db(app)