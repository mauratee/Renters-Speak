INSTRUCTIONS TO RUN RENTERS SPEAK WEB APP:

Use git clone or other method to copy entire contents of this repository to your local machine

Install dependencies from `requirements.txt` (`pip3 install` or other)

Run `source secrets.sh` in terminal to execute contents of `secrets.sh`

Enter `python3 seed_db.py`in terminal to seed database `testdb` with test data <br>

To view and query test database using SQL queries, enter `psql testdb` from terminal and enter (`\q` to exit)<br>
To query `testdb`using SQLAlchemy queries,  run `model.py` in interactive mode and use `quit()` to exit

TO RUN SERVER:<br>
Activate virtual environment by entering `source env/bin/activate` in terminal<br>
    Your command prompt should then show `(env)` at the beginning of the line<br>

In terminal, enter `python3 server.py`<br>
You should then see:<br>
    "Connected to the db!<br>
    * Serving Flask app 'server' (lazy loading)"<br>

Next, in a web browser, navigate to `http://localhost:5000/`<br>
You should then see the Renters Speak homepage!

To exit and stop running server, enter `CTRL + c` or `CMD + c`

TO RUN TESTS:<br>
In terminal, enter `python3 tests.py`<br>
Output will tell you how many test ran and how many failed of the tests that ran.

