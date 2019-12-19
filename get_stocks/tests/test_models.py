from django.test import TestCase
from get_stocks.models import Stock, FindStock, ViewStock

class TestModels(TestCase):

    def setUp(self):
        self.newProject = FindStock.objects.create(
            Symbol='AAPL',
            Interval='5min',
        )

    
    # def test_find_stocks_is_getting_data(self):
        
    #     self.assertEquals(self.newProject)
