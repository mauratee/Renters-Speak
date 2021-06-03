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