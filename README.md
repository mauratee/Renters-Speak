INSTRUCTIONS TO RUN RENTERS SPEAK WEB APP:

Run `source secrets.sh` to terminal to execute contents of `secrets.sh`

`db.create_all()` in python interactive, while running model.py to creates tables in database

`python3 seed_db.py`in terminal to seed database `testdb` with test data
to view and query test database using SQL queries, enter `psql testdb` from terminal (`\q` to exit)
OR run `model.py` in interactive mode to query test database via SQLAlchemy queries

TO RUN SERVER:
in terminal, enter `python3 server.py`
you should then see:
    Connected to the db!
    * Serving Flask app 'server' (lazy loading)
next, in a web browser, navigate to `http://localhost:5000/`
you should then see the Renters Speak homepage!

