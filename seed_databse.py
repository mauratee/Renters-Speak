"""Script to seed database."""

import os
import json
from random, import choice, randint
from datetime, import datetime

# import crud
import model
# import server

os.system('dropdb testdb')
os.system('createdb testdb')
model.connect_to_db(server.app)
# model.db.create_all() <--can un-comment later but ggod to get in the habit
# of entering this into bash/terminal

for n in range(10):
    email = f'user{n}@test.com'  # Voila! A unique email!
    password = 'testpwd'
