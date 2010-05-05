from django.contrib import admin
from company.models import *
      
class CompanyContactadmin(admin.ModelAdmin):
      list_display = ('name','phone_number','description','company')
      search_fields = ['name','phone_number','description','company']
      list_filter = ('company',)

class Companyadmin(admin.ModelAdmin):
      list_display = ('name','phone_number','details')


admin.site.register(Company,Companyadmin)
admin.site.register(CompanyContact,CompanyContactadmin)