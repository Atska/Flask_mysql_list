# media list
 This is a web-api for listing all my media I consumed and more 
 importantly still need to. The backend was created in python with the 
 help ob the web-framework Flask. For the Frontend Bootstrap and basic
 HTML/CSS was used. As the database mysql was chosen. No ORM was used so
 the codebase has sql-codes.

# Demo
![Screenshot](https://user-images.githubusercontent.com/54402396/69585884-389b9500-0fe1-11ea-9b32-e7fbc30ec44a.png)
# Quick start
1. Download the repository and use this command to install all 
required libaries
    pip install -r requirements.txt
2. 'register' your mysql account and host address in __init__ and 
create_sqldb.py
3. Create a new database in create_sqldb.py just by running the code
4. Add the name of the database in __init__ 
5. run the application in run_app.py
# libaries 
[flask quickstart](https://flask.palletsprojects.com/en/1.1.x/quickstart/#accessing-request-data)
Everything you want to know about flask is here.

[flask_mysqldb:](https://flask-mysqldb.readthedocs.io/en/latest/) Flask-MySQLdb provides MySQL connection for Flask.
# Bootstrap sources
Basic bootstrap code found on 
[getbootstrap.com.](https://getbootstrap.com/)

Examples:   
[Modals:](https://getbootstrap.com/docs/4.0/components/modal/)
Bootstrap’s JavaScript modal plugin adds dialogs to your site for 
lightboxes, user notifications, or completely custom content.

[Buttons:](https://getbootstrap.com/docs/4.0/components/buttons/)
Bootstrap’s custom button styles for actions in forms, dialogs, 
and more with support for multiple sizes, states, and more.

[Navbar:](https://getbootstrap.com/docs/4.0/components/navbar/)
Bootstrap’s powerful, responsive navigation header

[Forms:](https://getbootstrap.com/docs/4.3/components/forms/)
Examples and usage guidelines for form control styles, layout options, 
and custom components for creating a wide variety of forms.

# Mysql sources
[Official Website](https://dev.mysql.com/doc/connector-python/en/connector-python-examples.html)
