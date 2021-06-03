"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud # <-- un-comment after crud.py complete
import model 
# from model import db, User, Landlord, Building, Review, connect_to_db # <--delete if running seed_db.py works
import server

os.system('dropdb testdb')
os.system('createdb testdb')

model.connect_to_db(server.app)
model.db.create_all() # <-- can un-comment later but good to get in the habit
# of entering this into bash/terminal


# Create 10 test users
users_in_db = []

for n in range(10):
    email = f'user{n}@test.com'  # A unique email
    password = 'testpwd'

    user = crud.create_user(email, password)

    users_in_db.append(user)


# Create 10 test landlords
landlords_in_db = []

for n in range(10):
    landlord_name = f'Test Landlord {n}'
    street_num = randint(10, 2500)
    office_address = f'{street_num} Test Address Lane'

    landlord = crud.create_landlord(landlord_name, office_address)

    landlords_in_db.append(landlord)


# Create 5 test buildings
buildings_in_db = []
for n in range(5):
    street_num = randint(10, 2500)
    building_address = f'{street_num} Renters Road'
    landlord_to_own = choice(landlords_in_db)
    landlord_id=landlord_to_own.landlord_id

    building = crud.create_building(building_address, landlord_id)

    buildings_in_db.append(building)


# # Create 10 test reviews
# # test_review=Review(review_body="This is a test review.",
# #                   created_on=datetime.datetime(2020, 5, 23), 
# #                   updated_at=datetime.datetime(2020, 5, 23), 
# #                   user_id=test_user.user_id, 
# #                   building_id=test_building.building_id)

# for n in range(10):
#     review_body = f'This is test review number {n}.'
#     create_yr = randint(2017, 2020)
#     create_mth = randint(1, 12)
#     creat_day = randint(1, 28)
#     created_on = datetime.datetime(create_yr, create_mth, create_day)
#     updated_at = datetime.now()
#     user_to_write = choice(users_in_db)
#     building_to_write = choice(buildings_in_db)
#     review = Review(review_body=review_body, created_on=created_on, 
#                     updated_at=updated_at, user_id=user_to_write.user_id,
#                     building_id=building_to_write.building_id
#                     )
#     db.session.add(review)
#     db.session.commit()



