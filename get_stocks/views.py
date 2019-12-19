from django.shortcuts import render

# Create your views here.

#View for the home page 
#Just returns home.html 
def stock_list(request):

    return render(request, 'get_stocks/home.html')

