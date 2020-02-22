from django.test import TestCase
from get_stocks.models import Stock, FindStock, ViewStock

class TestModels(TestCase):

    #Testing if the model saves data to the DB 
    def setUp(self):
        self.newProject = FindStock.objects.create(
            Symbol='AAPL',
            Interval='5min',
        )

    
    # def test_find_stocks_is_getting_data(self):

    #     #entry = FindStock(Symbol='AAPL', Interval='5min')

    #     self.assertEqual('Symbol':'AAPL', 'Interval':'5min')
            
    #     #self.assertEqual(str(entry), entry.Symbol)
    #     #self.assertEqual(str(entry), entry.Interval)



        