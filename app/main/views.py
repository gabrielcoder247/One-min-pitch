from flask import render_template
from . import main



@main.route('/')
def index():

    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template('index.html') 
