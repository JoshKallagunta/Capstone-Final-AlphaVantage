from django.test import SimpleTestCase
from get_stocks.forms import NewSearch

class TestForms(SimpleTestCase):

    #Tests if the form is valid, using good data
    def test_new_search_form_IS_VALID(self):

        form = NewSearch(data={
            'Symbol' : 'AAPL',
            'Interval' : '5min'
        })

        self.assertTrue(form.is_valid())

    #Tests if the form is invaldid, using an empty Dict 
    def test_new_search_form_NO_DATA(self):

        form = NewSearch(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)


