from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm
import yfinance as yf
import pandas as pd

#decorators
#associates url from arag to the function below
@app.route('/') 
@app.route('/index', methods = ['GET', 'POST'])
def index():
    user = {'username': 'trums'}
    data = yf.download("SPY AAPL", start="2020-01-01", end="2020-09-25",
                   group_by="ticker")
    print(data)
    print(data.keys())
    print(data['SPY']['Close'])
    tickers = [
        {   'ticker': 'SPY',
            'price': data['SPY']['Close'][-1]
        },
        {
            'ticker': 'AAPL',
            'price': data['AAPL']['Close'][-1]
        }
    ]
    return render_template('index.html', title='Home', user=user, tickers=tickers)



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
