""" Models for landlord review site"""

import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """A user"""

    __tablename__ = "users"
    
    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    def __repr__(self):
        return f"<User user_id={self.user_id} email={self.email}>"


class Landlord(db.Model):
    """A landlord"""

    __tablename__ = "landlords"

    landlord_id = db.Column(db.Integer,
                            autoincrement=True,
                            primary_key=True)
    landlord_name = db.Column(db.String)
    office_address = db.Column(db.String)

    def __repr__(self):
        return f"<Landlord landlord_id={self.landlord_id} landlord_name={self.landlord_name}>"


class Building(db.Model):
    """A building"""

    __tablename__ = "buildings"

    building_id = db.Column(db.Integer,
                            autoincrement=True,
                            primary_key=True)
    building_address = db.Column(db.String)
    landlord_id = db.Column(db.Integer, # Foreign key from Building to landlord_id
                            db.ForeignKEy('landlords.landlord_id')
                            )


class Review(db.Model):
    """A review written by a user"""

    __tablename__ = "reviews"

    review_id = db.Column(db.Integer,
                            autoincrement=True,
                            primary_key=True)
    