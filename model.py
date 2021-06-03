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
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(25))

    # reviews = a list of Review objects, available from 
    # db.Relationship from Review class

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

    # buildingss = a list of Building objects, available from 
    # db.Relationship from Building class

    def __repr__(self):
        return f"<Landlord landlord_id={self.landlord_id} landlord_name={self.landlord_name}>"


class Building(db.Model):
    """A building
    
    fields: buiding_id,"""

    __tablename__ = "buildings"

    building_id = db.Column(db.Integer,
                            autoincrement=True,
                            primary_key=True)
    building_address = db.Column(db.String)
    landlord_id = db.Column(db.Integer, # Foreign key from Building to landlord_id
                            db.ForeignKey('landlords.landlord_id')
                            )
    
    # reviews = a list of Review objects, available from 
    # db.Relationship from Review class
    
    # Add relationship to Landlord class
    landlord = db.relationship('Landlord', backref='buildings')

    def __repr__(self):
        return f"<Building building_id={self.building_id} building_address={self.building_address}>"


class Review(db.Model):
    """A review written by a user"""

    __tablename__ = "reviews"

    review_id = db.Column(db.Integer,
                            autoincrement=True,
                            primary_key=True)
    review_body = db.Column(db.Text)
    created_on = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, # Foreign key from Review to user_id
                        db.ForeignKey('users.user_id')
                        )
    building_id = db.Column(db.Integer, # Foreign key from Review to building_id
                            db.ForeignKey('buildings.building_id')
                            )
    
    # Add relationship to User class
    user = db.relationship('User', backref='reviews') 
    # Add relationship to Building class
    building = db.relationship('Building', backref='reviews')

    def __repr__(self):
        return f"<Review review_id={self.review_id} created_on={self.created_on}>"


def connect_to_db(flask_app, db_uri='postgresql:///testdb', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app
    # from flask import Flask
    # app = Flask(__name__) <-- can delete if seed_db.py runs!

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)

