""" Models and database Schema for Renters Speak"""

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """A user"""

    __tablename__ = "users"
    
    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(25), nullable=False)

    # reviews = a list of Review objects, available from 
    # db.Relationship from Review class

    def __repr__(self):
        return f"<User user_id={self.user_id} email={self.email}, username={self.username}>"


class Landlord(db.Model):
    """A landlord"""

    __tablename__ = "landlords"

    landlord_id = db.Column(db.Integer,
                            autoincrement=True,
                            primary_key=True)
    landlord_name = db.Column(db.String)
    office_address = db.Column(db.String)

    # buildings = a list of Building objects, available from 
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
    # building_address = db.Column(db.String)
    building_housenumber = db.Column(db.Text)
    building_streetname = db.Column(db.Text)
    building_postcode = db.Column(db.String)
    landlord_id = db.Column(db.Integer, # Foreign key from Building to landlord_id
                            db.ForeignKey('landlords.landlord_id'), nullable=False
                            )
    
    # reviews = a list of Review objects, available from 
    # db.Relationship from Review class
    
    # Add relationship to Landlord class
    landlord = db.relationship('Landlord', backref='buildings')

    def __repr__(self):
        return f"""<Building building_id={self.building_id} building_housenumber=
                {self.building_housenumber} building_streetname={self.building_streetname}>"""


class Review(db.Model):
    """A review written by a user"""

    __tablename__ = "reviews"

    review_id = db.Column(db.Integer,
                            autoincrement=True,
                            primary_key=True)
    review_body = db.Column(db.Text)
    created_on = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
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


class HPDViolation(db.Model):
    __tablename__ = "hpd_violations"

    violationid = db.Column(db.Integer, primary_key=True)
    borough = db.Column(db.Text)
    housenumber = db.Column(db.Text)
    streetname = db.Column(db.Text)
    postcode = db.Column(db.String)
    apartment = db.Column(db.Text)
    novdescription = db.Column(db.Text) # Description of the violation
    violation_class = db.Column('class', db.String) # Python reserved keyword
    inspectiondate = db.Column(db.Date) # Date the violation was observed

    def __repr__(self):
        return f"""<HPDViolation violationid={self.violationid}, inspectiondate={self.inspectiondate}, 
                  address={self.housenumber} {self.streetname}, {self.postcode}>"""

class HPDRegistration(db.Model):
    __tablename__ = "hpd_registrations"

    registrationid = db.Column(db.Integer, primary_key=True)
    housenumber = db.Column(db.Text)
    streetname = db.Column(db.Text)
    postcode = db.Column('zip', db.Text)
    lastregistrationdate = db.Column(db.Date) # Date on which registration was processed
    registrationenddate = db.Column(db.Date) # Expiration of registration record

    def __repr__(self):
        return f"""<HPDRegistration registrationid={self.registrationid}, 
                    lastregistrationdate={self.lastregistrationdate}, 
                    address={self.housenumber} {self.streetname}, {self.postcode}>"""

class HPDContact(db.Model):
    __tablename__ = "hpd_contacts"

    registrationcontactid= db.Column(db.Integer, primary_key=True)
    registrationtype = db.Column('type', db.Text)
    contactdescription = db.Column(db.Text)
    corporationname = db.Column(db.Text)
    firstname = db.Column(db.Text) 
    lastname = db.Column(db.Text) 
    businesshousenumber = db.Column(db.Text)
    businessstreetname = db.Column(db.Text)
    businessapartment = db.Column(db.Text)
    businesscity = db.Column(db.Text)
    businessstate = db.Column(db.Text)
    businesszip = db.Column(db.Text)
    registrationid = db.Column(db.Integer, # Foreign key from Review to building_id
                          db.ForeignKey('hpd_registrations.registrationid'))
                          

    def __repr__(self):
        return f"""<HPDContact registrationcontactid={self.registrationcontactid}, 
                    registrationtype={self.registrationtype}>"""




def connect_to_db(flask_app, db_uri='postgresql:///testdb', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    # flask_app.config['SQLALCHEMY_ECHO'] = echo
    # flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)

