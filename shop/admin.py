from django.contrib import admin
from .models import *

# Register your models here.
class categadmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
    list_display=['name','slug']

admin.site.register(categ,categadmin)

class prodadmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
    list_display=['name','slug','img','price','stk','avbl','desc']
    list_editable=['price','stk','avbl','desc']
    
admin.site.register(products,prodadmin)