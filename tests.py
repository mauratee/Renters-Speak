from unittest import TestCase
from server import app
from model import db, User, Landlord, Building, Review, connect_to_db
from flask import session


class FlaskTestsBasic(TestCase):
    """Set up and run Flask tests"""

    def setUp(self):
        """Stuff to do before every test"""

        # Get the Flask test client
        self.client = app.test_client()

        # Show Flask errors that happen during tests
        app.config['TESTING'] = True



if __name__ == '__main__':
    import unittest

    unittest.main()