from django.test import SimpleTestCase
from get_stocks.forms import NewSearch

class TestForms(SimpleTestCase):

    def test_new_search_form_IS_VALID(self):

        form = NewSearch(data={
            'Symbol' : 'AAPL',
            'Interval' : '5min'
        })

        self.assertTrue(form.is_valid())
        #Pass


    def test_new_search_form_NO_DATA(self):

        form = NewSearch(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)
        #Pass


