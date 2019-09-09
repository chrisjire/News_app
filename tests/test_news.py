import unittest
from app.models import app

class SourcesTest(unittest.TestCase):
    '''
    Test Class to test the behavior of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Sources('CNN','CNN News','Cable News Network that is a leader in providing news worldwide','cnn.com','general','U.S.A','en')
