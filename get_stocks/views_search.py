from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.contrib import messages
from .models import FindStock
from .alphaAPI import alpha_api_call
from .forms import NewSearch

#
def view_search_stock(request):

    form = NewSearch()

    return render(request, 'get_stocks/searchStocks/searchstocks.html', {'form':form})



#
def display_stock_data_(request):

    if request.method == 'POST':

        form = NewSearch(request.POST)

        if form.is_valid():

            stock_name = form.cleaned_data.get('Symbol')
            interval_time = form.cleaned_data.get('Interval')
        
            stock_data = alpha_api_call(stock_name, interval_time)


            if stock_name is not None:

                try:
                    args = {'stock_name':stock_name, 'interval_time':interval_time, 'stock_data_html':stock_data.to_html() } 
                    return render (request, 'get_stocks/savedstocks/savedstocks.html', args)

                except AttributeError:

                    form = NewSearch()
                    messages.add_message(request, messages.ERROR, 'Sorry, invalid ticker symbol, please try again.')

                    return render(request, 'get_stocks/searchStocks/searchstocks.html', {'form':form})


        else:
            messages.add_message(request, messages.ERROR, 'Sorry, could not connnect to Alpha API.')

    else: 
        form = NewSearch()
        print('hello')
        return render(request, 'get_stocks/searchStocks/searchstocks.html', {'form': form} )

#AttributeError: 'NoneType' object has no attribute 'to_html'

