from app import app

#decorators
#associates url from arag to the function below
@app.route('/') 
@app.route('/index')

def index():
    return "Hello world"