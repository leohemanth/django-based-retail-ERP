from django.contrib import admin
from sale.models import *

class SaleItemsInline(admin.TabularInline):
    model = SaleInvoiceItem

class SaleInvoiceadmin(admin.ModelAdmin):
    inlines = [SaleItemsInline,]
    list_filter = ('customer','datetime')
    list_display = ('customer','datetime')
    search_fields = ['customer',]

admin.site.register(SaleInvoice,SaleInvoiceadmin)
admin.site.register(SaleItemsInline,SaleItemsInline)
