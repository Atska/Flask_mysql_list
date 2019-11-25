"""SQL-Code for creating the tables in the database from create_sqldb.py"""

Tables={}
Tables["buecher"] = (
    "CREATE TABLE Buecher ("
    "   ID INT UNSIGNED AUTO_INCREMENT,"
    "   title VARCHAR(50) NOT NULL,"
    "   author VARCHAR(50) NOT NULL,"
    "   genre VARCHAR(50) NOT NULL,"
    "   release_date DATE NOT NULL,"
    "   already_read VARCHAR(50) NOT NULL,"
    "   PRIMARY KEY (ID))"
    )

Tables["Serien"] = (
    "CREATE TABLE Serien ("
    "   ID INT UNSIGNED AUTO_INCREMENT,"
    "   title VARCHAR(50) NOT NULL,"
    "   episodes INT UNSIGNED NOT NULL,"
    "   aired DATE NOT NULL,"
    "   watched VARCHAR(50) NOT NULL,"
    "   PRIMARY KEY (ID))"
    )

Tables["Filme"] = (
    "CREATE TABLE Filme ("
    "   ID INT UNSIGNED AUTO_INCREMENT,"
    "   title VARCHAR(50) NOT NULL,"
    "   length INT UNSIGNED NOT NULL,"
    "   aired DATE NOT NULL,"
    "   watched VARCHAR(50) NOT NULL,"
    "   PRIMARY KEY (ID))"
    )
