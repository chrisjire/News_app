import urllib.request,json
from .models import News

#Getting api key
api_key = None

# Getting the new base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['API_KEY']
    base_url = app.config['API_BASE_URL']
    
def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        new_results = None

        if get_news_response['results']:
            new_results_list = get_news_response['results']
            new_results = process_results(new_results_list)
    
    return new_results