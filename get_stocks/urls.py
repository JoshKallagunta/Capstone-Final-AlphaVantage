from django.urls import path
from django.contrib import admin
from . import views, views_search, views_saved


app_name = 'get_stocks'

urlpatterns = [
    #Home page 
    path('', views.stock_list, name='stock_list'),

    #Track Stock page
    path('searchstocks/', views_search.view_search_stock, name='view_search_stock'),

    #View results of API call page 
    path('saved/', views_search.display_stock_data_, name='view_stock'),

    #In progress
    path('view_searches/', views_saved.view_all_saved_stocks, name='view_all_saved_stocks'),
    
]
