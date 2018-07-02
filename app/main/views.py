from flask import render_template
from . import main
from ..models import *

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting categories
    
    # pickupline = get_pickupline('pickup')
    pickupline = PickUp_line.query.all()
    # interview_pitch = get_interview('interview')
    # comment_pitch = get_comment('comment')
    # category_pitch = get_category('category')
    # product_pitch = get_product('product')
    # promotional_pitch = get_promotional('promotional')

    title = 'Home - Welcome to The best one minute pitch'

    # title = title, category = category_pitch,   
    # pickup = pickupline, interview = interview_pitch, comment = comment_pitch)
    return render_template('index.html', pickup = pickupline)