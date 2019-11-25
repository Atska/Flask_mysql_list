from flask import request, redirect, url_for, render_template, flash
from myapp import app
from myapp import mysql

@app.route('/', methods=['GET'])
def Startseite():
    return render_template('Startseite.html')

@app.route('/Serien', methods=['GET', 'POST'])
def Serien():
    cursor = mysql.connection.cursor()
    cursor.execute("    SELECT * FROM Serien   ")
    data = cursor.fetchall()
    cursor.close()
    return render_template('Serien.html', data=data)

@app.route('/Filme', methods=['GET', 'POST'])
def Filme():
    cursor = mysql.connection.cursor()
    cursor.execute("    SELECT * FROM Filme   ")
    data = cursor.fetchall()
    cursor.close()
    return render_template('Filme.html', data=data)

@app.route('/Buecher', methods=['GET', 'POST'])
def Buecher():
    cursor = mysql.connection.cursor()
    cursor.execute("    SELECT * FROM Buecher   ")
    data = cursor.fetchall()
    cursor.close()
    return render_template('Buecher.html', data=data)

@app.route('/Kontakt', methods=['GET','POST'])
def Kontakt():
    return render_template('Kontakt.html')

@app.route('/Spiele', methods=['GET', 'POST'])
def Spiele():
    return render_template('Spiele.html')

@app.route('/insertBooks', methods=['GET', 'POST'])
def insertBooks():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        genre = request.form['genre']
        release = request.form['release_date']
        read = request.form['already_read']

        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO Buecher (title, author, genre, release_date, already_read)"
                       "VALUES (%s, %s, %s, %s, %s)", (title, author, genre, release, read))
        mysql.connection.commit()
        flash('Daten wurden erfolgreich gespeichert!', 'success')
        return redirect(url_for('Buecher'))

@app.route('/updateBooks', methods=['GET', 'POST'])
def updateBooks():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        genre = request.form['genre']
        release_date = request.form['release']
        already_read = request.form['read']
        id_data = request.form['id']

        cursor = mysql.connection.cursor()
        cursor.execute("""
                        UPDATE buecher
                        SET title=%s, author=%s, genre=%s, release_date=%s, already_read=%s
                        WHERE id=%s
                        """, (title, author, genre, release_date, already_read, id_data))
        mysql.connection.commit()
        flash('Daten wurden erfolgreich gespeichert', 'success')
        return redirect(url_for('Buecher'))

@app.route('/deleteBooks/<string:id_data>', methods=['GET', 'POST'])
def deleteBooks(id_data):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM buecher WHERE id=%s", (id_data))
    mysql.connection.commit()
    flash('Daten wurden gelöscht!')
    return redirect(url_for('Buecher'))

@app.route('/orderBooks/<string:id_data>', methods=['GET', 'POST'])
def orderBooks():
    cursor = mysql.connection.cursor()
    cursor.execute("")


@app.route('/insertFilme', methods=['GET', 'POST'])
def insertFilme():
    if request.method == 'POST':
        title = request.form['title']
        length = request.form['length']
        aired = request.form['aired']
        watched = request.form['watched']

        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO Filme (title, length, aired, watched)"
                       "VALUES (%s, %s, %s, %s)", (title, length, aired, watched))
        mysql.connection.commit()
        flash('Daten wurden erfolgreich gespeichert!', 'success')
        return redirect(url_for('Filme'))

@app.route('/updateFilme', methods=['GET', 'POST'])
def updateFilme():
    if request.method == 'POST':
        title = request.form['title']
        length = request.form['length']
        aired = request.form['aired']
        watched = request.form['watched']
        id_data = request.form['id']

        cursor = mysql.connection.cursor()
        cursor.execute("""
                        UPDATE FILME
                        SET title=%s, length=%s, aired=%s, watched=%s
                        WHERE id=%s
                       """, (title, length, aired, watched, id_data))
        mysql.connection.commit()
        flash('Daten wurden erfolgreich gespeichert!', 'success')
        return redirect(url_for('Filme'))

@app.route('/deleteFilme/<string:id_data>', methods=['GET', 'POST'])
def deleteFilme(id_data):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM Filme WHERE id=%s", (id_data))
    mysql.connection.commit()
    flash('Daten wurden gelöscht!')
    return redirect(url_for('Filme'))

@app.route('/insertSerien', methods=['GET', 'POST'])
def insertSerien():
    if request.method == 'POST':
        title = request.form['title']
        episodes = request.form['episodes']
        aired = request.form['aired']
        watched = request.form['watched']

        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO Serien (title, episodes, aired, watched)"
                       "VALUES (%s, %s, %s, %s)",
                       (title, episodes, aired, watched))
        mysql.connection.commit()
        flash('Daten wurden erfolgreich gespeichert!', 'success')
        return redirect(url_for('Serien'))

@app.route('/updateSerien', methods=['GET', 'POST'])
def updateSerien():
    if request.method == 'POST':
        title = request.form['title']
        episodes = request.form['episodes']
        aired = request.form['aired']
        watched = request.form['watched']
        id_data = request.form['id']

        cursor = mysql.connection.cursor()
        cursor.execute("""
                        UPDATE Serien
                        SET title=%s, episodes=%s, aired=%s, watched=%s
                        WHERE id=%s
                       """, (title, episodes, aired, watched, id_data))
        mysql.connection.commit()
        flash('Daten wurden erfolgreich gespeichert!', 'success')
        return redirect(url_for('Serien'))

@app.route('/deleteSerien/<string:id_data>', methods=['GET', 'POST'])
def deleteSerien(id_data):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM Serien WHERE id=%s", (id_data))
    mysql.connection.commit()
    flash('Daten wurden gelöscht!')
    return redirect(url_for('Serien'))
