from django.contrib import admin
from product.models import *


class Categoryadmin(admin.ModelAdmin):
    list_display = ('name','description')
    search_fields = ['name','description']



class Productadmin(admin.ModelAdmin):
    list_display = ('name','description','shortcut','category','image')
    list_filter = ('name','description','shortcut','category')
    search_fields = ['name','description','shortcut']

admin.site.register(Product,Productadmin)
admin.site.register(Category,Categoryadmin)
