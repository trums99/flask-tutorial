from app import app
from flask import render_template, flash, redirect
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


#'GET' requests are those that return info to the client
#'POST' requests are usually when browser submits form data to the server


@app.route('/login', methods = ['GET', 'POST']) #accepts get and post, override default
def login():
    form = LoginForm()
    if form.validate_on_submit(): #processes the form (submit button pressed)
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form = form)
