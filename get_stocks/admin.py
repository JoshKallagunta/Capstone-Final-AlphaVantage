from django.contrib import admin
from .models import Stock, FindStock

# Register your models here.

admin.site.register(Stock)
admin.site.register(FindStock)

