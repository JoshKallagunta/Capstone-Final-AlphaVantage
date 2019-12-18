from django.shortcuts import render

# Create your views here.
def stock_list(request):

    return render(request, 'get_stocks/home.html')

