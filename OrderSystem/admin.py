from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ('pid', 'name', 'weight', 'retail')

class UserAdmin(admin.ModelAdmin):
    list_display = ('uid', 'username', 'password')

class OrderListAdmin(admin.ModelAdmin):
    list_display = ('listid', 'user', 'date', 'ship', 'shipcost', 'total')

class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ('orderid', 'productid', 'amount')

class ShipAdmin(admin.ModelAdmin):
    list_display = ('type', 'shipname', 'price')

admin.site.register(Product, ProductAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(OrderList, OrderListAdmin)
admin.site.register(OrderDetail, OrderDetailAdmin)
admin.site.register(Ship, ShipAdmin)

# Register your models here.
