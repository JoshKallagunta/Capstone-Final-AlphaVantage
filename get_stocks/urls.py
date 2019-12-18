from django.urls import path
from django.contrib import admin
from . import views, views_search, views_saved


app_name = 'get_stocks'

urlpatterns = [
    path('', views.stock_list, name='stock_list'),

    path('searchstocks/', views_search.view_search_stock, name='view_search_stock'),

    path('saved/', views_search.display_stock_data_, name='view_stock'),
    
]
