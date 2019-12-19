from django.shortcuts import render
from .models import ViewStock

#View for the output of the API call 
def view_saved_stock(request):

    return render(request, 'get_stocks/savedstocks/savedstocks.html')



    