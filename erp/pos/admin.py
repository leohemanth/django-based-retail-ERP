from django.contrib import admin
from erp.pos.models import invoice,sale

class invoiceadmin(admin.ModelAdmin):
    list_display = ('customer_name', 'invoice_no','address','date','time')
    search_fields = ('customer_name', 'invoice_no','address','date','time')

class saleadmin(admin.ModelAdmin):
    list_display = ('quantity',)
    search_fields = ('quantity',)
    filter_horizontal = ('product',)
admin.site.register(invoice,invoiceadmin)
admin.site.register(sale,saleadmin)