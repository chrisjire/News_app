from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_news

# Views
@main.route('/')
def index():
    
    '''
    View root page function that returns the index page and its data
    '''

    # Getting news
    top_headlines = get_news('top_headlines')
    all_articles = get_news('all_articles')
    sources = get_news('sources')
    
    title = 'Home - Welcome to The best News Review Website Online'
    
    
    return render_template('index.html', title = title, top_headlines = top_headlines, all_articles = all_articles, now_showing = sources )
