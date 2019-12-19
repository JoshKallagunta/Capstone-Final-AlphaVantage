from django.test import TestCase, Client
from django.urls import reverse, resolve
from get_stocks.views import stock_list
from get_stocks.views_search import view_search_stock, display_stock_data_
from get_stocks.views_saved import view_saved_stock
from get_stocks.models import FindStock


class TestViews(TestCase):


    def setUp(self):
        self.client = Client()
        self.stock_search = FindStock.objects.create(
            Symbol = 'MSFT',
            Interval = '5min'
        )



    def test_invalid_symbol_shows_error_message(self):
        # arrange - set up the state of the app
        invalid_stock_data = { 'Symbol': '12345', 'Interval': '5min'}

        # action
        response = self.client.post(reverse('get_stocks:view_stock'), invalid_stock_data , follow=True)
        
        # assert  - did everything happen as expected? 
        self.assertEquals(200, response.status_code)
        self.assertIn('invalid ticker symbol', str(response.content))


    def test_invalid_interval_shows_error_message(self):
        # arrange - set up the state of the app
        invalid_stock_data = { 'Symbol': 'goog', 'Interval': 'sidfjdfogjdifog'}

        # action
        response = self.client.post(reverse('get_stocks:view_stock'), invalid_stock_data , follow=True)
        
        # assert  - did everything happen as expected? 
        self.assertEquals(200, response.status_code)
        self.assertIn('sidfjdfogjdifog is not one of the available choices', str(response.content))    



    def test_view_url_exists_at_HOME_PAGE_GET(self):

        response = self.client.get(reverse('get_stocks:stock_list'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'get_stocks/home.html')


    def test_view_url_exists_at_SEARCHSTOCKS_GET(self):

        response = self.client.get(reverse('get_stocks:view_search_stock'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'get_stocks/searchStocks/searchstocks.html')


    def test_view_url_exists_at_SAVEDSTOCKS_Output_GET(self):

        response = self.client.get(reverse('get_stocks:view_stock'))

        self.assertEqual(response.status_code, 200)

        #Changed urls (really should be get_stocks/savedstocks/savedstocks.html)
        #Possible reroute 
        self.assertTemplateUsed(response, 'get_stocks/searchStocks/searchstocks.html')


    def test_view_search_DISPLAY_STOCK_DATA_POST(self):

        ui_input = self.stock_search

        response = self.client.post(reverse('get_stocks:view_stock'), {
            'Symbol':'MSFT',
            'Interval':'5min'
        }, follow=True)

        print(response)
        self.assertEquals(response.status_code, 302)
        # assert you land on the stock details page 
        self.assertTemplateUsed('')
        self.assertIn('MSFT Prices', str(response.content))



    







