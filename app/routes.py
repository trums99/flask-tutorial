from app import app
from flask import render_template

#decorators
#associates url from arag to the function below
@app.route('/') 
@app.route('/index')

def index():
    user = {'username': 'trums'}
    return render_template('index.html', title='Home', user=user)
