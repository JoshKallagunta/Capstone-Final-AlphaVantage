from django.test import TestCase
from django.urls import reverse, resolve
from get_stocks.views import stock_list
from get_stocks.views_search import view_search_stock, display_stock_data_
from get_stocks.views_saved import view_saved_stock


class TestViews(TestCase):

    def test_view_url_exists_at_HOME_PAGE(self):
        response = self.client.get('get_stocks/home.html')
        self.assertEqual(response.status_code, 200)
