from django.contrib import admin
from purchase.models import *

class Paymentadmin(admin.ModelAdmin):
   list_display = ('mode','description','invoice')
   list_filter = ('mode','description','invoice')


class PurchaseInvoiceItemadmin(admin.ModelAdmin):
   list_display = ('invoice','product','quantity','price')
   list_filter = ('invoice','product')
     

class PurchaseItemsInline(admin.TabularInline):
   model = PurchaseInvoiceItem
    

class PurchaseInvoiceadmin(admin.ModelAdmin): 
   inlines = [PurchaseItemsInline,]
   list_filter = ('company','datetime')
   list_display = ('company','datetime')
   search_fields = ['company',]

admin.site.register(Payment,Paymentadmin)
admin.site.register(PurchaseInvoiceItem,PurchaseInvoiceItemadmin)
admin.site.register(PurchaseInvoice,PurchaseInvoiceadmin)
