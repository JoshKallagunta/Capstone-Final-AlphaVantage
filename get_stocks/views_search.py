from django.shortcuts import render, redirect, HttpResponseRedirect
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

    print('joshua')
    print('interval_time')

    if request.method == 'POST':
        form = NewSearch(request.POST)

        if form.is_valid():

            stock_name = form.cleaned_data.get['Symbol']
            interval_time = form.cleaned_data.get['Interval']

            #stock_name, interval_time = alpha_api_call()

            stock_data = alpha_api_call(stock_name, interval_time)


            if stock_name is not None:

                args = {'stock_name':stock_name, 'interval_time':interval_time, 'stock_data':stock_data } 
                return render (request, 'get_stocks/savedstocks/savedstocks.html', args)
            
            else:
                messages.add_message(request, messages.ERROR, 'Sorry, could not connnect to Alpha API.')

    else: 
        form = NewSearch()
        print('hello')
        return render(request, 'get_stocks/searchStocks/searchstocks.html', {'form': form} )

