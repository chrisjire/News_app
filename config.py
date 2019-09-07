import os
from newsapi import NewsApiClient


class Config:
    '''
    General configuration parent class
    '''
    API_BASE_URL = 'https://newsapi.org/v2/sources?apiKey=db4ec7c57e644b949ddf0e238f3c1436'
    API_KEY = os.environ.get('API_KEY')



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
    
config_options = {
'development':DevConfig,
'production':ProdConfig
}