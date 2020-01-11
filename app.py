
from flask import Flask, escape, url_for, request, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('login.html')


@app.route('/admin')
def admin():
    return 'This is admin page'


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/home')
def home():
    return render_template('home.html')

##############################################


@app.route('/<temp>')
def name_page(temp):
    return 'Hello {}!'.format(temp)


@app.route('/get_post_test', methods=['GET', 'POST', 'PUT'])
def get_post_test():
    if request.method == 'GET':
        return 'this_is_get'
    elif request.method == 'POST':
        return 'this_is_post'
    elif request.method == 'PUT':
        return 'this_is_post'


with app.test_request_context():
    print(url_for('hello'))
    print(url_for('admin'))
