from flask import Flask
from flask_mysqldb import MySQL
import os

app = Flask(__name__)

# secrets.token_hex(16)
app.config['SECRET_KEY'] = '19f003c178f09d5ac56ccb6907b906c1'
# Username and password are saved as system variables
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER')
app.config['MYSQL_PASSWORD']= os.environ.get('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = 'Medien'
mysql = MySQL(app)

from myapp.routes import urls
# create_app():
