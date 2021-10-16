"""
Routes covered by this file:
/
/new_user
/login
/logout
/reviews
"""

from unittest import TestCase
from server import app, session # import app and session from server
from model import db, User, Landlord, Building, Review, HPDViolation, HPDRegistration, HPDContact, connect_to_db
import os


class FlaskTestsBasic(TestCase):
    """Set up and run Flask tests"""

    def setUp(self):
        """Stuff to do before every test"""

        # Get the Flask test client
        self.client = app.test_client()

        # Show Flask errors that happen during tests
        app.config['TESTING'] = True

        # Set up secret key in order to use "session"
        app.config['SECRET_KEY'] = 'key'

    def test_index(self):
        """Test homepage."""

        result = self.client.get("/")
        self.assertIn(b"Navigation", result.data)
        

class FlaskTestsNewUSer(TestCase):
    """Test new user creation route."""

    def setUp(self):
        """Stuff to do before every test: get Flask test client, show errors, 
            set up secret key"""

        self.client = app.test_client()
        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'key'

    def tearDown(self):
        """Stuff to do at end of every test."""

        # Remove user from database that was created in test_new_user_route
        user = User.query.filter(User.email == "newuser@gmail.com").first()
        if user:
            db.session.delete(user)
            db.session.commit()

    def test_new_user_route(self):
        """Check that a new user can be created and stored in 'users' database."""

        with self.client as c:

            result = c.post("/new_user",
                            data={"email": "newuser@gmail.com", "username": "test_user",
                            "password": "pwd543"}, follow_redirects=True)
            # Database query to "Users" that returns user object that matches "newuser@gmail.com"
            db_query = User.query.filter(User.email == "newuser@gmail.com").first()

            self.assertEqual("newuser@gmail.com", db_query.email)


class FlaskTestsLogInLogOut(TestCase):
    """Test user log in and log out."""

    def setUp(self):
        """Stuff to do before every test: get Flask test client, show errors, 
            set up secret key"""

        self.client = app.test_client()
        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'key'

        # Create new user in database
        user = User(email="email@gmail.com", username="user_name", password="password123")
        
        db.session.add(user)
        db.session.commit()
    
    def tearDown(self):
        """Stuff to do at end of every test."""

        # Remove user from database that was created in setUp
        user = User.query.filter(User.email == "email@gmail.com").first()
        db.session.delete(user)
        db.session.commit()
        
    def test_login_route(self):
        """Check that the login route adds user to session for user already in DB."""

        with self.client as c:

            result = c.post("/login",
                            data={"email": "email@gmail.com", "password": "password123"},
                            follow_redirects=True)

            self.assertEqual(session["user_email"], "email@gmail.com")

    def test_logout_route(self):
        """Check that logout route removes user from sesssion for logged in user
            who is already in DB."""

        with self.client as c:
            with c.session_transaction() as sess:
                sess["user_email"] = "email@gmail.com"

            result = self.client.get("/logout", follow_redirects=True)

            self.assertNotIn(b"user_email", session)



class FlaskTestsLoggedIn(TestCase):
    """Flask tests with user logged in to session."""
    
    def setUp(self):
        """Stuff to do before every test."""

        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'key'
        self.client = app.test_client()

        with self.client as c:
            with c.session_transaction() as sess:
                sess['user_email'] = "user4@test.com"
    
    def test_write_review_form(self):
        """Check that the write review form shows up in the all_reviews page
            for users that are logged in."""

        result = self.client.get("/reviews")
        self.assertIn(b"Write a Review", result.data)


class FlaskTestsLoggedOut(TestCase):
    """Flask tests with no user logged in to session."""

    def setUp(self):
        """Stuff to do before every test."""

        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'key'
        self.client = app.test_client()

    def test_no_review_form(self):
        """Check that the write review form does not show up in the all_reviews 
            page for users that are not logged in."""

        result = self.client.get("/reviews")
        self.assertNotIn(b"Write a Review", result.data)



if __name__ == '__main__':
    import unittest
    # Connect to app from server
    connect_to_db(app)
    unittest.main()

    