from flask import render_template
from app import app

@app.route('/')
def index():

    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template('index.html') 
