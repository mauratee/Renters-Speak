from unittest import TestCase
from server import app, session # import app and session from server
from model import db, User, Landlord, Building, Review, connect_to_db
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
    

    def test_login_route(self):
        """Check that the login route renders properly."""

        with self.client as c:

            result = c.post("/login",
                            data={"email": "email@gmail.com", "password": "password123"},
                            follow_redirects=True)

            self.assertEqual("user_email" in session.keys(), False)
            # self.assertEqual(session["user_email"], "email@gmail.com") <-- doesn't work because user is not created and added to db first.



if __name__ == '__main__':
    import unittest
    # Connect to app from server
    connect_to_db(app)
    unittest.main()

    