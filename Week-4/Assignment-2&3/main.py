from flask import Flask, render_template, request, session, redirect
from flask.helpers import url_for
import pymysql.cursors
import re
import json

app = Flask(__name__)
app.secret_key = 'your secret key'




connection = pymysql.connect(
    host = "localhost",
    user = "root",
    passwd = "1234",
    database = "assignment",
    cursorclass=pymysql.cursors.DictCursor
)

cursor = connection.cursor()

# Create DATABASE
# cursor.execute("DROP DATABASE IF EXISTS assignment" )
# cursor.execute("CREATE DATABASE IF NOT EXISTS assignment")

# Create TABLE
cursor.execute("DROP TABLE IF EXISTS user")
cursor.execute("CREATE TABLE IF NOT EXISTS `user` (`id` int(11) AUTO_INCREMENT PRIMARY KEY, `email` varchar(32), `password` varchar(32))")


sql = "INSERT INTO user (`email`, `password`) VALUES (%s, %s)"
cursor.execute(sql, ('test@gmail.com', 'pwd'))
connection.commit()



# def register_db():
#     sql = "INSERT INTO `user` (`email`, `password`) VALUES (%s, %s)"
#     cursor.execute(sql, (f"{request.form['email']}", "{request.form['password']}"))
#     connection.commit()


# def check_db():
#     query = f"SELECT * FROM user WHERE email = '{request.form['email']}'"
#     cursor.execute(query)
#     result = cursor.fetchone()
#     print(result['email'])






@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = request.form
    if request.method == 'POST' and 'email' in form and 'password' in form:
        email = form['email']
        password = form['password']
        cursor.execute("SELECT * FROM user WHERE email = %s AND password = %s", (email, password,))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['email'] = account['email']
            msg =  "Logged In, Welcome"
            return redirect(url_for('member'))
        else:
            msg = "Oops! Incorrect email / password"
            return render_template('index.html', msg=msg)
    return render_template('index.html')



@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('email', None)
    session.pop('password', None)
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = request.form
    msg = ''
    if request.method == 'POST' and 'email' in form and 'password' in form:
        email = form['email']
        password = form['password']
        cursor.execute("SELECT * FROM user WHERE email = %s", (email, ))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', password):
            msg = 'Username must contain only characters and numbers!'
        elif not password or not email:
            msg = 'Please fill out the form!'
        else:
            query = "INSERT INTO user (`email`, `password`) VALUES (%s, %s)"
            cursor.execute(query, (email, password,))
            connection.commit()
            return redirect(url_for('login'))
        # return render_template('member.html', msg=msg)
    elif request.method == 'POST':
        msg = 'Please fill out the form'
    return render_template('register.html', msg=msg)


@app.route('/member')
def member():
    if 'loggedin' in session:
        return render_template('member.html', email=session['email'])
    return redirect(url_for('login'))


@app.route('/profile')
def profile():
    if 'loggedin' in session:
        cursor.execute("SELECT * FROM user WHERE id = %s", (session['id'], ))
        account = cursor.fetchone()
        return render_template('profile.html', account=account)
    return redirect(url_for('login'))


@app.route('/data', methods=['GET', 'POST'])
def data():
    url = 'http://13.230.176.178:4000/api/1.0/remote-w4-data'
    return render_template('home.html')



if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')
