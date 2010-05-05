from django.contrib import admin
from pos.models import *

class ProductPriceadmin(admin.ModelAdmin):
     list_display = ('product','selling_price','datetime')
     list_filter = ('product','datetime')
     search_fields = ['product','datetime']

class Categoryadmin(admin.ModelAdmin):
      list_display = ('name','description')
      search_fields = ['name','description']
      
class CompanyContactadmin(admin.ModelAdmin):
      list_display = ('name','phone_number','description','company')
      search_fields = ['name','phone_number','description','company']
      list_filter = ('company',)

admin.site.register(ProductPrice,ProductPriceadmin)
class Paymentadmin(admin.ModelAdmin):
       list_display = ('mode','description','invoice')
       list_filter = ('mode','description','invoice')

admin.site.register(Payment,Paymentadmin)
admin.site.register(CompanyContact,CompanyContactadmin)
class Companyadmin(admin.ModelAdmin):
     list_display = ('name','phone_number','details')

admin.site.register(Company,Companyadmin)
class Customeradmin(admin.ModelAdmin):
     list_display = ('name','phone_number','details')

admin.site.register(Customer,Customeradmin)
admin.site.register(Category,Categoryadmin)

class PurchaseInvoiceItemadmin(admin.ModelAdmin):
     list_display = ('invoice','product','quantity','price')
     list_filter = ('invoice','product')
     
class SaleItemsInline(admin.TabularInline):
    model = SaleInvoiceItem

class SaleInvoiceadmin(admin.ModelAdmin):
    inlines = [SaleItemsInline,]
    list_filter = ('customer','datetime')
    list_display = ('customer','datetime')
    search_fields = ['customer',]

class PurchaseItemsInline(admin.TabularInline):
    model = PurchaseInvoiceItem
    

class PurchaseInvoiceadmin(admin.ModelAdmin):
    inlines = [PurchaseItemsInline,]
    list_filter = ('company','datetime')
    list_display = ('company','datetime')
    search_fields = ['company',]

class Productadmin(admin.ModelAdmin):
    list_display = ('name','description','shortcut','category')
    list_filter = ('name','description','shortcut','category')
    search_fields = ['name','description','shortcut']

admin.site.register(PurchaseInvoiceItem,PurchaseInvoiceItemadmin)
admin.site.register(PurchaseInvoice,PurchaseInvoiceadmin)
admin.site.register(SaleInvoice,SaleInvoiceadmin)
admin.site.register(Product,Productadmin)
