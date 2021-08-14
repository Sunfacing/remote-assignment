import json
from flask import (Flask, request, render_template, 
                    make_response, redirect, url_for)



PORT=3000
HOST='0.0.0.0'

app = Flask(__name__)

"""""""""""""""""""""""""""""
       Assignment-1 & 4
"""""""""""""""""""""""""""""

@app.route('/')
@app.route('/<name>')
def index(name='My Server'):
    name = request.args.get('name', name)
    data = getcookie()   # Assignemnt-4 get cookie
    if data:
        greeting = f"Hello, {data}!"
    else:
        greeting = f"Hello, {name}!"  
    return render_template('index.html', greeting=greeting)
    


"""""""""""""""""""""""""""""
       Assignment-2 & 3
"""""""""""""""""""""""""""""
@app.route('/data', methods=['GET', 'POST'])
def data(number="Lack of Parameter"):
    number = request.args.get('number', number)     
    if number == "Lack of Parameter": 
        return number
    else:
        try:
            num = int(number)
            sum = 0
            for i in range(1, num + 1):
                sum += i
            return str(sum) 

        except ValueError:
            return 'Wrong Parameter, please type an integar'


@app.route('/sum.html')
@app.route('/sum')
def sum():
    return render_template('sum.html')


"""""""""""""""""""""""""""""
       Assignment-4
"""""""""""""""""""""""""""""
@app.route('/login', methods=['GET', 'POST'])
def login():
    data = getcookie()
    return render_template('login.html', name=data)



@app.route('/trackName', methods=['GET', 'POST'])
def trackName():
    if request.method == 'POST':
        user = request.form['name']
        response = make_response(redirect(url_for('index')))
        response.set_cookie('userID', user)
        return response



@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('userID')
    print (name)
    return name 



if __name__=='__main__':
    app.run(debug=True, port=PORT, host=HOST)