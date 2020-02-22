from django.test import SimpleTestCase
from django.urls import reverse, resolve
from get_stocks.views import stock_list
from get_stocks.views_search import view_search_stock, display_stock_data_
from get_stocks.views_saved import view_saved_stock 


class TestUrls(SimpleTestCase):

    #Tests if Stock_list is going to the correct view/html page 
    def test_stock_list_is_resolved(self):

        url = reverse('get_stocks:stock_list')
        self.assertEquals(resolve(url).func, stock_list)

    #Tests if Search_stock is going to the correct view/html page 
    def test_view_search_stock_is_resolved(self):

        url = reverse('get_stocks:view_search_stock')
        self.assertEquals(resolve(url).func, view_search_stock)

    #Tests if View_stock is going to the correct view/html page 
    def test_view_stock_is_resolved(self):

        url = reverse('get_stocks:view_stock')
        self.assertEquals(resolve(url).func, display_stock_data_)

