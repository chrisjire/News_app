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

def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
    new_results = []
    for new_item in new_list:
        id = new_item.get('id')
        title = new_item.get('original_title')
        overview = new_item.get('overview')
        poster = new_item.get('poster_path')
        

        if poster:
            new_object = News(id,title,overview,poster)
            new_results.append(new_object)


    return new_results

def get_news(id):
    get_new_details_url = base_url.format(id,api_key)
    
    with urllib.request.urlopen(get_new_details_url) as url:
        new_details_data = url.read()
        new_details_response = json.loads(new_details_data)
        
        new_object = None
        if new_details_response:
            id = new_details_response.get('id')
            title = new_details_response.get('original_title')
            overview = new_details_response.get('overview')
            poster = new_details_response.get('poster_path')

            new_object = News(id,title,overview,poster)

    return new_object