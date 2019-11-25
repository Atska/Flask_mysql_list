import mysql.connector as mysql
from mysql.connector import errorcode
from myapp.mysqlData import mysql_tables
import os

# Variable Name of the created database
DB_Name = "Medien"

# API to connect python with mysql
new_db = mysql.connect(
    host = "localhost",
    user = os.environ.get('MYSQL_USER'),
    password = os.environ.get('MYSQL_PASSWORD'),
    auth_plugin = "mysql_native_password"
    )

# Create cursor to execute commands from python to mysql
cursor = new_db.cursor()

def create_database():
    """Create the database with DB_Name as its name."""
    try:
        cursor.execute("CREATE DATABASE {}".format(DB_Name))
    # If there is no database, error occurs
    except mysql.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

# Try finding the db with that name.
try:
    cursor.execute("USE {}".format(DB_Name))
# If there is no database. execute create_database()
except mysql.Error as err:
    print("Database {} does not exists.".format(DB_Name))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database()
        print("Database {} created successfully.".format(DB_Name))
        new_db.database = DB_Name
    else:
        print(err)
        exit(1)

# Extract tables from other file
Tables = mysql_tables.Tables
for table_name in mysql_tables.Tables:
    header = Tables[table_name]
    try:
        print("{}: ".format(table_name))
        cursor.execute(header)
    # If error occurs because the table exists, print the message
    except mysql.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")
