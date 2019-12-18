from django.test import TestCase
from get_stocks.models import Stock, FindStock, ViewStock

class TestModels(TestCase):

    def setUp():
        self.newProject = FindStock.objects.create(
            name = 'APPL',
            interval = '1min'
        )

    
    #def test_find_stocks_is_getting_data(self):
        
        #self.assertEquals(self.newProject)
