from django.shortcuts import render
from .models import ViewStock, FindStock

#View for the output of the API call 
def view_saved_stock(request):

    return render(request, 'get_stocks/savedstocks/savedstocks.html')

#In Progress
#Getting all searched data and displaying it on a page 
def view_all_saved_stocks(request):
    stocks_objects = FindStock.objects.all()

    return render(request, 'get_stocks/savedstocks/view_searches.html', {'stock_objects':stocks_objects})



    