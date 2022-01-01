from django.contrib import admin
from django.contrib.admin.decorators import action
from .models import Products
from .models import Order
# Register your models here.

admin.site.site_header = "E-commerce site"
admin.site.site_title = "ABC shop"
admin.site.index_title = "Manage shop"



class ProductAdmin(admin.ModelAdmin):

    def change_category_to_default(self,request,queryset):
        queryset.update(category="default")

    change_category_to_default.short_description = 'Deafult category'
    list_display = ('title','price','discount_price','category','description','image')
    search_fields = ('title',)
    actions = ('change_category_to_default',)
    list_editable = ('price','discount_price',)



admin.site.register(Products,ProductAdmin)
admin.site.register(Order)