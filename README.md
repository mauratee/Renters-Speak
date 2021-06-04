INSTRUCTIONS TO RUN RENTERS SPEAK WEB APP:

Run `source secrets.sh` to terminal to execute contents of `secrets.sh`

Enter `python3 seed_db.py`in terminal to seed database `testdb` with test data <br>

To view and query test database using SQL queries, enter `psql testdb` from terminal and enter (`\q` to exit)<br>
To query `testdb`using SQLAlchemy queries,  run `model.py` in interactive mode and use `quit()` to exit

TO RUN SERVER:
In terminal, enter `python3 server.py`<br>
You should then see:<br>
    Connected to the db!<br>
    * Serving Flask app 'server' (lazy loading)<br>
Next, in a web browser, navigate to `http://localhost:5000/`<br>
You should then see the Renters Speak homepage!

