from django.contrib import admin
from customer.models import *

class Customeradmin(admin.ModelAdmin):
     list_display = ('name','phone_number','details')

class Categoryadmin(admin.ModelAdmin):
     list_display = ('name','description')
     search_fields = ['name','description']

      
      

admin.site.register(Customer,Customeradmin)
admin.site.register(Category,Categoryadmin)
