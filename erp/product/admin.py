from django.contrib import admin
from erp.product.models import product, group

class productadmin(admin.ModelAdmin):
    list_display = ('name', 'desc')
    search_fields = ('name', 'desc')
    filter_horizontal = ('group',)
admin.site.register(product,productadmin)
admin.site.register(group)
