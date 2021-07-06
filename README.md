[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

# ✨ About this Project
Renters Speak gives users a peek behind the curtain of the New York City rental market. Designed for renters looking for more information about their current or prospective landlords, this app provides a platform for users to write and share reviews of landlords and also presents data related to building ownership and building maintenance violations from NYC housing datasets. Users can search for information by address and Renters Speak provides reviews and housing data in an easy to understand, visually appealing format.

## Technologies Used:
### Languages:
<ul>
<li>Python 3</li>
<li>JavaScript</li>
<li>SQL</li>
<li>CSS</li>
<li>HTML 5</li>
<li>Flask</li>
<li>SQLAlchemy</li>
<li>Flask-SQLAlchemy</li>
</ul>

### Libraries/Frameworks:
<ul>
<li>Python unittest</li>
<li>Flask test_client</li>
<li>PostgreSQL</li>
<li>Flask</li>
<li>SQLAlchemy</li>
<li>Flask-SQLAlchemy</li>
<li>Jinja 2</li>
<li>AJAX</li>
<li>jQuery</li>
<li>jQuery UI</li>
<li>Chart.js</li>
<li>Bootstrap</li> 
</ul>

### APIs:
<ul>
<li>Google Maps for JavaScript API</li>
<li>NYC Geosearch API</li>
<li>NYC housing datasets via NYCDB</li>
</ul>

## Instructions to Run Renters Speak Web App:

Use `git clone` or other method to copy entire contents of this repository to your local machine

Install dependencies from `requirements.txt` (`pip3 install`, `python3 -m pip install` or other)

Run `source secrets.sh` in terminal to execute contents of `secrets.sh`

Enter `python3 seed_db.py`in terminal to seed database `testdb` with test data <br>

To view and query test database using SQL queries, enter `psql testdb` from terminal and enter (`\q` to exit)<br>
To query `testdb`using SQLAlchemy queries,  run `model.py` in interactive mode and use `quit()` to exit

### To Run Server:
Activate virtual environment by entering `source env/bin/activate` in terminal<br>
    Your command prompt should then show `(env)` at the beginning of the line<br>

In terminal, enter `python3 server.py`<br>
You should then see:<br>
    "Connected to the db!<br>
    * Serving Flask app 'server' (lazy loading)"<br>

Next, in a web browser, navigate to `http://localhost:5000/`<br>
You should then see the Renters Speak homepage!

To exit and stop running server, enter `CTRL + c` or `CMD + c`

To Seed Database:
in shell:
    `dropdb testdb`
    `createdb testdb`
    `nycdb -U hackbright -D testdb --load hpd_registrations` <!-- loads hpd_registrations and hpd_contacts tables, takes about 2 mins -->
    `nycdb -U hackbright -D testdb --load hpd_violations`<!-- creates SQL table in testdb
    hpd_violations rows should load, will take about 20-50 mins -->
run model.py interactively: `python3 -i model.py`
    `db.create_all()` <!-- creates all other tables in testdb -->
in shell:
    `python3 seed_db.py` <!-- Commented out lines to dropdb, createdb and db.create_all() -->


### To Run Tests:
In terminal, enter `python3 tests.py`<br>
The output will tell you how many tests ran and how many failed of the tests that ran.

## 👏 Acknowledgements
Thanks to the New York Housing Data Coalition, the programmers of NYCDB, and my teachers, classmates and mentors at the Hackbright Academy Engineering Fellowship.

