"""CRUD operations for landlord review site"""

import datetime
from model import db, User, Landlord, Building, Review, connect_to_db


def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user


def create_landlord(landlord_name, office_address):
    """Create and return a new landlord."""

    landlord = Landlord(landlord_name=landlord_name, office_address=office_address)

    db.session.add(landlord)
    db.session.commit()

    return landlord


def create_building(building_address, landlord_id):
    """Create and return a new building."""

    building = Building(building_address=building_address, landlord_id=landlord_id)

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


def get_building_by_address(address):
    """Takes in building address as argument and checks if building exists in "buildings"
        database. If building exists, returns building object. If building does not
        exist, returns None."""
    
    return Building.query.filter(Building.building_address == address).first()


def get_landlord_by_id(landlord_id):
    """Takes in landlord id as argument and checks if landlord exists in "landlords"
        database. If landlord exists, returns landlord object. If landlord does not
        exist, returns None."""
    
    return Landlord.query.filter(Landlord.landlord_id == landlord_id).first()


def get_landlord_by_name(landlord_name):
    """Takes in landlord name as argument and checks if landlord exists in "landlords"
        database. If landlord exists, returns landlord object. If landlord does not
        exist, returns None."""
    
    return Landlord.query.filter(Landlord.landlord_name == landlord_name).first()


def get_user_by_id(user_id):
    """Takes in user id and checks if user exists in "users" database.
        If user exists, return user object. If user does not exist, return None."""

    return User.query.filter(User.user_id == user_id).first()


def get_user_by_email(email):
    """Takes in email address and checks if email exists in "users" database.
        If user exists, return user object. If user does not exist, return None."""
    
    return User.query.filter(User.email == email).first()


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


if __name__ == '__main__':
    from server import app
    connect_to_db(app)