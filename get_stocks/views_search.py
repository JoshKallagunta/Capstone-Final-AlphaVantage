from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.contrib import messages
from .models import FindStock
from .alphaAPI import alpha_api_call
from .forms import NewSearch

#View for creating a new empty form 
#Used in the searchstocks.html 
def view_search_stock(request):

    form = NewSearch()

    return render(request, 'get_stocks/searchStocks/searchstocks.html', {'form':form})



#Calls class alphaAPI.py class 
#Uses the form to do the API request and returns a dataframe of the data 
def display_stock_data_(request):

    #If the method is POST, will populate the NewSearch form with user input 
    if request.method == 'POST':

        form = NewSearch(request.POST)

        #Checks if form is valid
        #If valid, Sends the user input to the the API with the form data, using paramaters 
        if form.is_valid():

            stock_name = form.cleaned_data.get('Symbol')
            interval_time = form.cleaned_data.get('Interval')
        
            stock_data = alpha_api_call(stock_name, interval_time)

            #If there is valid data and the API call is successful, it will return the data on to the savedstocks.html page 
            #Since stock_data is returning a dataframe, using .html to display data in a table 
            if stock_name is not None:

                try:
                    args = {'stock_name':stock_name, 'interval_time':interval_time, 'stock_data_html':stock_data.to_html(classes='table table-striped') } 
                    return render (request, 'get_stocks/savedstocks/savedstocks.html', args)

                #If the stock_name is not a real ticker symbol, catches that error, creates a new form,
                #and prints the user a helpful message / redirects them back to the form page
                except AttributeError:

                    form = NewSearch()
                    messages.add_message(request, messages.ERROR, 'Sorry, invalid ticker symbol, please try again.')

                    return render(request, 'get_stocks/searchStocks/searchstocks.html', {'form':form})

        #If API connection is unsuccessful, gives the user a message 
        else:
            messages.add_message(request, messages.ERROR, 'Sorry, could not connnect to Alpha API.')

            return render(request, 'get_stocks/searchStocks/searchstocks.html', {'form':form})


    #If the method is a GET request(more than likely), it will generate a new form on the searchstocks.html page 
    else: 
        form = NewSearch()
        return render(request, 'get_stocks/searchStocks/searchstocks.html', {'form': form} )


