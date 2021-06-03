Make sure you `createdb testdb`
`createdb` in terminal, as bash command (not interactive)
`db.create_all()` in python interactive, while running model.py to creates tables in database
`python3 seed_db.py`in terminal to seed database `testdb` with test data
to view and query test database using SQL queries, enter `psql testdb` from terminal OR
run `model.py` in interactive mode to query test database via SQLAlchemy queries

TO RUN SERVER:
in terminal, enter `python3 server.py`
you should then see:
Connected to the db!
 * Serving Flask app 'server' (lazy loading)
 then, in a web browser, navigate to `http://localhost:5000/`

