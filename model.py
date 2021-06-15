""" Models for landlord review site"""

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
    building_address = db.Column(db.String)
    landlord_id = db.Column(db.Integer, # Foreign key from Building to landlord_id
                            db.ForeignKey('landlords.landlord_id'), nullable=False
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


class HpdViolation(db.Model):
    __tablename__ = "hbd_violations"

    violation_id = db.Column("ViolationID", db.Integer, primary_key=True)
    house_number = db.Column("HouseNumber", db.Text)
    street_name = db.Column("StreetName", db.Text)
    post_code = db.Column("Postcode", db.String)
    apt_num = db.Column("Apartment", db.Text)
    violation_class = db.Column("Class", db.String)
    inspection_date = db.Column("InspectionDate", db.Date)

    def __repr__(self):
        return f"""<hbd_violations violation_id={self.violation_id}, inspection_date={self.inspection_date}, 
                  address={self.house_number} {self.street_name}, {self.post_code}>"""


def connect_to_db(flask_app, db_uri='postgresql:///testdb', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)

