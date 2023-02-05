# import mysqldb.cursors
import re

import pymysql as MySQLdb
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
from mysql.connector import cursor

app = Flask(__name__)

app.secret_key = 'abc-der'

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'newuser'
app.config['MYSQL_PASSWORD'] = '12345'
app.config['MYSQL_DB'] = 'mydata'

mysql = MySQL(app)


@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        conn = MySQLdb.connect(
            host='127.0.0.1',
            user='newuser',
            password='12345',
            db='mydata',
        )
        curr = conn.cursor()
        curr.execute('SELECT * FROM user WHERE email = % s AND password = % s', (email, password,))
        user = curr.fetchone()
        print(email, 'before')
        print(password)
        print(user)
        if user:
            session['logged_in'] = True
            session[email] = user[2]
            session[password] = user[3]
            print(session[email])
            print(session[password])
            message = 'Logged in successfully !'
            print("hello")
            return redirect(url_for('users', message=message))
        else:
            print("else hello")
            message = 'Please enter correct email / password !'
    return render_template('login.html', message=message)


@app.route('/logout')
def logout():
    global message
    if 'logged_in' in session:
        session.pop('logged_in', None)
        session.pop('userid', None)
        session.pop('email', None)
        session.pop('name', None)
        message = 'logged out successfully !'
    return render_template('login.html', message=message)


@app.route("/users", methods=['GET', 'POST'])
def users():
    message = ""
    print(session.get('logged_in'))
    if session.get('logged_in') == True:
        conn = MySQLdb.connect(
            host='127.0.0.1',
            user='newuser',
            password='12345',
            db='mydata',
        )
        curr = conn.cursor()
        curr.execute('SELECT * FROM user')
        users = curr.fetchall()
        message = "listed all the users"
        return render_template("users.html", users=users, message=message)
    return redirect(url_for('login'))


@app.route('/view', methods=['GET', 'POST'])
def view():
    conn = MySQLdb.connect(
        host='127.0.0.1',
        user='newuser',
        password='12345',
        db='mydata',
    )
    curr = conn.cursor()
    curr.execute('SELECT * FROM user')
    db_users = curr.fetchall()

    # Close cursor after fetching data
    curr.close()

    users = [
        [1, "user1", "user1@example.com", "password1", "admin", "USA"],
    ]
    # Add the additional list of users to the database users
    users = db_users
    return render_template('view.html', users=users)


@app.route('/change_password', methods=['GET', 'POST'])
def change_password():
    message = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        confirm_pass = request.form['confirm_pass']
        conn = MySQLdb.connect(
            host='127.0.0.1',
            user='newuser',
            password='12345',
            db='mydata',
        )
        curr = conn.cursor()
        curr.execute('SELECT * FROM user WHERE email = % s AND password = % s', (email, password,))
        user = curr.fetchone()
        if user:
            curr.execute('UPDATE user SET password = % s WHERE email = % s', (confirm_pass, email,))
            conn.commit()
            message = 'Password updated successfully !'
        else:
            message = 'Please enter correct email / password !'
    return render_template('change_password.html', message=message)


@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if 'logged_in' in session:
        userid = request.form['userid']
        conn = MySQLdb.connect(
            host='127.0.0.1',
            user='newuser',
            password='12345',
            db='mydata'
        )
        curr = conn.cursor()
        curr.execute("DELETE FROM `user` WHERE userid = %s", (userid,))
        conn.commit()
    return redirect(url_for('users'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if 'logged_in' in session:
        if request.method == 'POST' and 'name' in request.form and 'email' in request.form and 'password' in request.form and 'role' in request.form and 'country' in request.form:
            name = request.form['name']
            email = request.form['email']
            password = request.form['password']
            role = request.form['role']
            country = request.form['country']
            print(name)
            if not re.match(r'[A-Za-z0-9]+', name):
                msg = 'Name must contain only characters and numbers!'
            elif not re.match(r'[^@]+@[^@]+.[^@]+', email):
                msg = 'Invalid email address!'
            elif not re.match(r'[A-Za-z0-9]+', password):
                msg = 'Password must contain only characters and numbers!'
            else:
                conn = MySQLdb.connect(
                    host='127.0.0.1',
                    user='newuser',
                    password='12345',
                    db='mydata',
                )
                curr = conn.cursor()
                curr.execute('INSERT INTO user (name, email, password, role, country) VALUES (%s, %s, %s, %s, %s)',
                             (name, email, password, role, country))
                conn.commit()
                msg = 'User created successfully!'
            return redirect(url_for('users', msg=msg))
        elif request.method == 'POST':
            msg = 'Please fill out the form!'
        return render_template('register.html', msg=msg)
    return redirect(url_for('users'))


if __name__ == '__main__':
    app.run(debug=True, port=8000)
