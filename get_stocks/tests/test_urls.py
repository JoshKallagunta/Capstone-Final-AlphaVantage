from django.test import SimpleTestCase
from django.urls import reverse, resolve
from get_stocks.views import stock_list
from get_stocks.views_search import view_search_stock, display_stock_data_
from get_stocks.views_saved import view_saved_stock 


class TestUrls(SimpleTestCase):

    def test_stock_list_is_resolved(self):

        url = reverse('stock_list')
        print(resolve(url))
        self.assertEquals(resolve(url).func, stock_list)
        #NoReverseMatch


    def test_view_search_stock_is_resolved(self):

        url = reverse('view_search_stock')
        print(resolve(url))
        self.assertEquals(resolve(url).func, view_search_stock)
        #NoReverseMatch

    def test_view_stock_is_resolved(self):

        url = reverse('view_stock')
        print(resolve(url))
        self.assertEquals(resolve(url).func, view_saved_stock)
        #NoReverseMatch

