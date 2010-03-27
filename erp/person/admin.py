from django.contrib import admin
from erp.person.models import person, group

class personadmin(admin.ModelAdmin):
    list_display = ('name','address','city','state','phone1_type','phone1','phone2_type','phone2','phone3_type','phone3','phone4_type','phone4','phone5_type','phone5','phone6_type','phone6','email1','email2','website1','email1','email2','website1','website2','others',
)
    search_fields = ('name','address','city','state','phone1_type','phone1','phone2_type','phone2','phone3_type','phone3','phone4_type','phone4','phone5_type','phone5','phone6_type','phone6','email1','email2','website1','email1','email2','website1','website2','others',
)
    filter_horizontal = ('group',)
admin.site.register(person,personadmin)
admin.site.register(group)
