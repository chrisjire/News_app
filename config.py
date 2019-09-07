import os


class Config:
    '''
    General configuration parent class
    '''
    NEWS_SOURCES_BASE_URL ='https://newsapi.org/v2/sources?language=en&category={}&apiKey=db4ec7c57e644b949ddf0e238f3c1436'
    ARTICLES_BASE_URL = 'https://newsapi.org/v2/everything?language=en&sources={}&apiKey=db4ec7c57e644b949ddf0e238f3c1436'
    API_KEY = os.environ.get('API_KEY')
    @staticmethod
    def init_app(app):
            pass


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