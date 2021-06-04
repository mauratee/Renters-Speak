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


def create_review(review_body, created_on, updated_at, user_id, building_id):
    """Create and return a new review."""

    review = Review(review_body=review_body, created_on=created_on, 
                    updated_at=updated_at, user_id=user_id,
                    building_id=building_id)
    
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


def get_user_by_email(email):
    """Takes in email address and checkes if email exists in "users" database.
        If user exists, return user_id. If user does not exist, return None."""
    
    # if email in users,
    #   return user_id
    # else
    #   return None


if __name__ == '__main__':
    from server import app
    connect_to_db(app)