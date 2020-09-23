from app import app
from flask import render_template
from app.forms import LoginForm

#decorators
#associates url from arag to the function below
@app.route('/') 
@app.route('/index')


def index():
    user = {'username': 'trums'}
    posts = [
        {
            'author': {'username': 'kms'},
            'body': 'fadkfjadflkadjfdfdfa'
        },
        {
            'author': {'username': 'pepega'},
            'body': 'fadkfjadflkadjfdfdfa'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form = form)
