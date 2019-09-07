from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_news,get_new,search_new

# Views
@main.route('/')
def index():
    
    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular new
    popular_news = get_news('popular')
    upcoming_new = get_news('upcoming')
    now_showing_new = get_news('now_playing')
    
    title = 'Home - Welcome to The best new Review Website Online'
    
    search_new = request.args.get('new_query')
    
    if search_new:
        return redirect(url_for('search',new_name = search_new))
    else:
        return render_template('index.html', title = title, popular = popular_news, upcoming = upcoming_new, now_showing = now_showing_new )
