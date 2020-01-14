
from flask import Flask, escape, url_for, request, render_template

from flask_admin import Admin

app = Flask(__name__)


app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

admin = Admin(app, name='My Backedn',
              base_template='https://bootswatch.com/3/cyborg/bootstrap.css',  template_mode='bootstrap3')

app.run()


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/temp')
def admin():
    return 'This is temp page'


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     error = None
#     print(request)
#     print(request.args.username)
#     if request.method == 'POST':
#         if valid_login(request.form['username'], request.form['password']):
#             return 'login Successfully'
#         else:
#             error = 'Invalid username or password'
#     return render_template('login.html', error=error)


def valid_login(username, password):
    if username == 'akhil' and password == '123':
        return true
    else:
        return false

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
