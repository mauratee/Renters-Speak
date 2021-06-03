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